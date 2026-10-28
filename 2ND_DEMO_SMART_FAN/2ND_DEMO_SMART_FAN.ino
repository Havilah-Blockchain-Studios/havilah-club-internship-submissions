#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <HTTPClient.h>
#include <DHT.h>

// =====================================================================
//  SMART FAN - ESP32-S3
//  Changes in this version:
//   - n8n sync now runs in a background task (the fan, alarm, button
//     and dashboard no longer freeze when n8n is unreachable)
//   - n8n only changes mode/set point when n8n's value CHANGES, so it
//     no longer overwrites your button or slider every 10 seconds
//   - ngrok URL uses https://
//   - safer parsing of n8n replies
//   - relay polarity setting, named constants, smaller functions
//   - works on ESP32 Arduino core 2.x and 3.x
// =====================================================================

// ---------- Type your own values here ----------
// Do NOT share this file publicly (GitHub, reports) with the real passwords in it.
const char* WIFI_SSID  = "DEVICE NAME ";          // Exact name, including any trailing space
const char* WIFI_PASS  = "WIFI PASSWORD";
const char* N8N_SECRET = "N8N SECRET";     // Same secret as in the n8n Code nodes
String n8nBase = "LAPTOP ADDRESS";      // Laptop address (changes if the laptop's IP changes)
const char* CHAT_URL = "http://<YOUR_LOCAL_IP>:5678/webhook/<YOUR_WEBHOOK_ID>/chat";
const char* CHAT_URL_PUBLIC = "https://<YOUR_NGROK_DOMAIN>.ngrok-free.dev/webhook/<YOUR_WEBHOOK_ID>/chat";
// ---------- Sensor ----------
const int PIN_DHT = 4;           // DHT22 on GPIO 4 (with 10k pull-up to 3.3V)
#define SENSOR_TYPE DHT22
DHT dht(PIN_DHT, SENSOR_TYPE);

// ---------- Pins ----------
const int PIN_FAN    = 5;    // PWM signal to NPN gate driver
const int PIN_BTN    = 6;    // Mode push button to GND
const int PIN_BUZZER = 7;    // Buzzer NPN driver base
const int PIN_RELAY  = 8;    // Relay module trigger
const int PIN_LED_R  = 1;    // Red LED
const int PIN_LED_G  = 2;    // Green LED
const int PIN_LED_B  = 3;    // Blue LED (GPIO 3 is a strapping pin on ESP32-S3: if boot is ever flaky, move this LED)
const int PIN_PIR    = 18;   // HC-SR501 PIR sensor

// ---------- Settings ----------
float TEMP_ON = 30.0, TEMP_OFF = 28.0, TEMP_FULL = 35.0;
const float TEMP_DANGER = 38.0;
const int  MIN_DUTY = 90;                         // Lowest speed that still spins the fan
const int  FAILSAFE_DUTY = 160;                   // Speed when the sensor is broken
const int  MANUAL_DUTY = 200;                     // Speed in "Fan on" mode
const int  PWM_FREQ = 20000;                      // 20 kHz
const int  FAN_CHANNEL = 0;                       // Only used on ESP32 core 2.x
const unsigned long READ_MS = 2000;               // Sensor read interval
const unsigned long PRESENCE_HOLD_MS = 10000;     // 10 s presence timeout
const unsigned long PIR_WARMUP_MS = 60000;        // 60 s PIR warm-up
const unsigned long RELAY_MIN_ON_MS = 5000;       // Relay stays closed at least 5 s
const unsigned long RELAY_SETTLE_MS = 150;        // Wait after the relay closes before spinning the fan
const unsigned long RAMP_MS = 20;                 // Speed changes every 20 ms
const int  RAMP_UP = 5;                           // Speed step up
const int  RAMP_DOWN = 10;                        // Speed step down
const unsigned long BTN_DEBOUNCE_MS = 200;
const int  DHT_FAILS_ALLOWED = 3;                 // Failed reads in a row before "sensor fault"
const unsigned long SYNC_MS = 10000;              // n8n sync every 10 s
const bool USE_RELAY = true;                      // Master relay is in the circuit
const bool RELAY_ACTIVE_HIGH = true;              // Set to false if your relay module clicks on when the pin is LOW
const bool DANGER_OVERRIDES_OFF = true;           // true = fan switches on at 38C even in "Fan off" mode or with nobody present

enum Mode { AUTO_PRESENCE, AUTO_DEMO, MANUAL_ON, OFF_MODE };
const char* modeNames[] = {"Auto + presence", "Auto (demo)", "Fan on", "Fan off"};

// ---------- State ----------
Mode mode = AUTO_PRESENCE;
float fakeTemp = 25.0, temp = 25.0, humidity = NAN;
bool useFake = false, fakeFault = false, sensorOk = true, fanOn = false, lastBtn = HIGH;
bool present = false, alarmState = false, relayOn = false, dangerFan = false;
int duty = 0, target = 0, prevTarget = 0, dhtFails = 0;
unsigned long lastRead = 0, lastMotion = 0, lastRamp = 0, lastBtnMs = 0, relayMs = 0;
unsigned long lastPrint = 0, lastWifi = 0;

// ---------- Shared with the background n8n task ----------
volatile bool cloudOk = false;       // set by the task
volatile bool syncNow = false;       // set by the "s" serial command
volatile bool remoteNew = false;     // task -> loop: a fresh reply is waiting
volatile int  remoteSp = -1, remoteMode = -1;
int  lastRemoteSp = -1, lastRemoteMode = -1;   // what n8n said last time
bool remoteSeeded = false;
SemaphoreHandle_t n8nLock;           // protects n8nBase

WebServer server(80);

// ---------- Web page ----------
const char PAGE[] PROGMEM = R"rawliteral(
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Smart Fan</title>
      <style>
        body{font-family:sans-serif;margin:0;padding:16px;background:#f2f4f7;color:#1b2430}
        h1{margin:0 0 12px;font-size:22px}
        .card{background:#fff;border-radius:12px;padding:14px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,.1)}
        .row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #eee}
        .row:last-child{border-bottom:none}
        .big{font-size:44px;font-weight:700}
        .badge{display:inline-block;padding:4px 12px;border-radius:12px;color:#fff;font-weight:600}
        button{padding:12px;margin:4px 2px;border:none;border-radius:8px;background:#1f3a5f;color:#fff;font-size:15px}
        button.on{background:#2e7d32}
        input[type=range]{width:100%}
        small{color:#667}
      </style>
    </head>
      
    <body>
      <h1>Smart Fan</h1>

      <div class="card">
        <div class="big"><span id="temp">--</span> &deg;C</div>
        <span id="state" class="badge" style="background:#1565c0">--</span>
        <div id="alarm" style="color:#c62828;font-weight:700"></div>
      </div>

      <div class="card">
        <div class="row"><span>Fan speed</span><b id="speed">--</b></div>
        <div class="row"><span>Mode</span><b id="mode">--</b></div>
        <div class="row"><span>Set point</span><b id="setpoint">--</b></div>
        <div class="row"><span>Humidity</span><b id="hum">--</b></div>
        <div class="row"><span>Temperature from</span><b id="src">--</b></div>
        <div class="row"><span>Someone present</span><b id="present">--</b></div>
        <div class="row"><span>Sensor</span><b id="sensor">--</b></div>
        <div class="row"><span>n8n link</span><b id="cloud">--</b></div>
        <div class="row"><span>Last update</span><b id="age">--</b></div>
      </div>

      <div class="card">
        <b>Mode</b><br>
        <button id="m0" onclick="send('/mode?m=0')">Auto + presence</button>
        <button id="m1" onclick="send('/mode?m=1')">Auto (demo)</button>
        <button id="m2" onclick="send('/mode?m=2')">Fan on</button>
        <button id="m3" onclick="send('/mode?m=3')">Fan off</button>
      </div>

      <div class="card">
        <b>Set point: <span id="spv">30</span> &deg;C</b> <small>(22 to 35)</small>
        <input type="range" id="sp" min="22" max="35" step="1" value="30"
          oninput="document.getElementById('spv').textContent=this.value"
          onchange="send('/setpoint?v='+this.value)">
      </div>

      <div class="card">
        <b>Voice</b> <small>(tap Talk, then say for example: set the fan to 26)</small><br>
        <button id="talk" onclick="talk()">&#127908; Talk</button>
        <div id="vmsg" style="margin-top:8px;white-space:pre-line"></div>
      </div>

      <div class="card" id="testcard">
        <b>Test controls</b> <small>(the test temperature overrides the real sensor)</small><br>
        Test temperature: <b id="tv">25</b> &deg;C
        <input type="range" id="tt" min="15" max="45" step="0.5" value="25"
          oninput="document.getElementById('tv').textContent=this.value"
          onchange="send('/temp?v='+this.value)">
        <button onclick="send('/real')">Use real sensor</button>
        <button onclick="send('/motion')">Simulate motion</button>
      </div>

      <script>
      window.CHAT_LOCAL = '%%CHAT_LOCAL%%';
      window.CHAT_PUBLIC = '%%CHAT_PUBLIC%%';
      window.CHAT_NOW = (location.protocol === 'https:' && window.CHAT_PUBLIC) ? window.CHAT_PUBLIC : window.CHAT_LOCAL;
      </script>

      <script>
        var last = 0;
        function $(id){return document.getElementById(id);}
        function send(p){fetch(p).then(refresh).catch(function(){});}
        function refresh(){
          fetch('/status').then(function(r){return r.json();}).then(function(d){
            last = Date.now();
            $('temp').textContent = d.temp.toFixed(1);
            $('speed').textContent = Math.round(d.duty/255*100) + ' %';
            $('mode').textContent = d.mode;
            $('setpoint').textContent = d.setpoint + ' \u00b0C';
            $('hum').textContent = d.hum >= 0 ? d.hum + ' %' : '--';
            $('src').textContent = d.fake ? 'Test value' : 'Real sensor';
            $('present').textContent = d.present ? 'Yes' : 'No';
            $('sensor').textContent = d.sensor ? 'OK' : 'FAULT';
            $('cloud').textContent = d.cloud ? 'Connected' : 'Not connected';
            var s = $('state');
            if(!d.sensor){s.textContent='Sensor fault';s.style.background='#8e24aa';}
            else if(d.temp < d.setpoint){s.textContent='Cool';s.style.background='#1565c0';}
            else if(d.temp < d.full){s.textContent='Warm';s.style.background='#f9a825';}
            else{s.textContent='Hot';s.style.background='#c62828';}
            $('alarm').textContent = d.alarm ? 'ALARM: overheating or sensor fault' : '';
            for(var i=0;i<4;i++){ $('m'+i).className = (i==d.modeIdx) ? 'on' : ''; }
            if(document.activeElement !== $('sp')){ $('sp').value = d.setpoint; $('spv').textContent = d.setpoint; }
          }).catch(function(){ $('age').textContent = 'offline'; });
        }
        setInterval(refresh, 2500);
        setInterval(function(){ if(last) $('age').textContent = Math.round((Date.now()-last)/1000) + ' s ago'; }, 1000);
        refresh();

        if (location.protocol === 'https:') { var tc = $('testcard'); if (tc) tc.style.display = 'none'; }

        var sid = 'voice-' + Math.random().toString(36).slice(2);
        function vmsg(t){ $('vmsg').textContent = t; }

        function parseReply(t){
          try { var j = JSON.parse(t); return j.output || j.text || ''; } catch(e) {}
          var out = '';
          t.split('\n').forEach(function(l){
            try { var j = JSON.parse(l); if (j.type === 'item' && j.content) out += j.content; } catch(e) {}
          });
          return out || t;
        }

        function askBot(text){
          var url = window.CHAT_NOW;
          if(!url){ vmsg('No chat address is set in the sketch.'); return; }
          vmsg('You said: ' + text + '\nAsking the chatbot...');
          var h = {'Content-Type':'application/json'};
          if (location.protocol === 'https:') h['ngrok-skip-browser-warning'] = 'true';
          fetch(url, {method:'POST', headers:h,
                      body: JSON.stringify({action:'sendMessage', sessionId:sid, chatInput:text})})
            .then(function(r){ return r.text(); })
            .then(function(t){
              var out = parseReply(t);
              vmsg('You said: ' + text + '\nBot: ' + out);
              try { speechSynthesis.cancel(); speechSynthesis.speak(new SpeechSynthesisUtterance(out)); } catch(e) {}
            })
            .catch(function(){ vmsg('Could not reach the chatbot.'); });
        }

        function talk(){
          if(!window.isSecureContext){
            vmsg('The microphone only works on a secure (HTTPS) page. This page is plain HTTP, so use the chat bubble below and type instead.');
            return;
          }
          var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
          if(!SR){ vmsg('This browser has no speech recognition.'); return; }
          var r = new SR();
          r.lang = 'en-NG';
          r.interimResults = false;
          r.maxAlternatives = 1;
          r.onstart = function(){ vmsg('Listening...'); $('talk').className = 'on'; };
          r.onresult = function(e){ askBot(e.results[0][0].transcript); };
          r.onerror = function(e){ vmsg('Microphone problem: ' + e.error); };
          r.onend = function(){ $('talk').className = ''; };
          r.start();
        }
      </script>
      
      <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet">
      
      <div id="n8n-chat"></div>
      
      <script type="module">
        import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';
        var u = window.CHAT_NOW;
        var cfg = { webhookUrl: u, target: '#n8n-chat', mode: 'window', initialMessages: ['Hi! I can help with the fan.'] };
        if (location.protocol === 'https:') cfg.webhookConfig = { method: 'POST', headers: { 'ngrok-skip-browser-warning': 'true' } };
        if (u) createChat(cfg);
      </script>
    </body>
  </html>
)rawliteral";

// ---------- Small helpers ----------
void fanPwm(int value) {
#if ESP_ARDUINO_VERSION_MAJOR >= 3
  ledcWrite(PIN_FAN, value);
#else
  ledcWrite(FAN_CHANNEL, value);
#endif
}

void relayWrite(bool on) {
  digitalWrite(PIN_RELAY, (on == RELAY_ACTIVE_HIGH) ? HIGH : LOW);
}

void applySetpoint(int v) {
  TEMP_ON = v;
  TEMP_OFF = v - 2;
  TEMP_FULL = (v + 5.0f < TEMP_DANGER) ? (v + 5.0f) : TEMP_DANGER;
}

// ---------- Web handlers ----------
void handleRoot() {
  String html = String(PAGE);
  html.replace("%%CHAT_LOCAL%%", CHAT_URL);
  html.replace("%%CHAT_PUBLIC%%", CHAT_URL_PUBLIC);
  server.send(200, "text/html", html);
}

void handleStatus() {
  char buf[512];
  int hum = isnan(humidity) ? -1 : (int)humidity;
  snprintf(buf, sizeof(buf),
    "{\"temp\":%.1f,\"hum\":%d,\"fake\":%d,\"duty\":%d,\"mode\":\"%s\",\"modeIdx\":%d,\"setpoint\":%d,\"full\":%.1f,"
    "\"present\":%d,\"sensor\":%d,\"alarm\":%d,\"cloud\":%d}",
    temp, hum, useFake ? 1 : 0, duty, modeNames[mode], (int)mode, (int)TEMP_ON, TEMP_FULL,
    present ? 1 : 0, sensorOk ? 1 : 0, alarmState ? 1 : 0, cloudOk ? 1 : 0);
  server.send(200, "application/json", buf);
}

void handleMode() {
  int m = server.arg("m").toInt();
  if (server.hasArg("m") && m >= 0 && m <= 3) {
    mode = (Mode)m;
    Serial.print("Mode: "); Serial.println(modeNames[mode]);
    server.send(200, "text/plain", "ok");
  } else server.send(400, "text/plain", "bad mode");
}

void handleSetpoint() {
  int v = server.arg("v").toInt();
  if (server.hasArg("v") && v >= 22 && v <= 35) {
    applySetpoint(v);
    Serial.printf("Set point: %d\n", v);
    server.send(200, "text/plain", "ok");
  } else server.send(400, "text/plain", "outside safe range");
}

void handleTemp() {
  float v = server.arg("v").toFloat();
  if (server.hasArg("v") && v >= 0 && v <= 60) {
    fakeTemp = v; useFake = true; fakeFault = false;
    Serial.printf("Test temperature set to %.1f\n", fakeTemp);
    server.send(200, "text/plain", "ok");
  } else server.send(400, "text/plain", "bad temperature");
}

void handleReal() {
  useFake = false;
  Serial.println("Using real sensor");
  server.send(200, "text/plain", "ok");
}

void handleMotion() {
  lastMotion = millis();
  Serial.println("Motion detected");
  server.send(200, "text/plain", "ok");
}

// ---------- n8n link (runs in its own background task) ----------
// Returns the whole number after "key": or -1 if it is missing or not a plain number.
int jsonInt(const String& s, const char* key) {
  String k = String("\"") + key + "\":";
  int i = s.indexOf(k);
  if (i < 0) return -1;
  i += k.length();
  while (i < (int)s.length() && s[i] == ' ') i++;
  if (i >= (int)s.length() || !isDigit(s[i])) return -1;
  return s.substring(i).toInt();
}

void syncN8n() {
  static bool prevCloud = false;
  int code = 0;
  bool ok = false;

  if (WiFi.status() == WL_CONNECTED) {
    String base;
    xSemaphoreTake(n8nLock, portMAX_DELAY);
    base = n8nBase;
    xSemaphoreGive(n8nLock);

    HTTPClient http;
    http.setConnectTimeout(2000);
    http.setTimeout(2500);
    if (http.begin(base + "/webhook/fan-sync")) {
      http.addHeader("Content-Type", "application/json");
      char body[360];
      int hum = isnan(humidity) ? -1 : (int)humidity;
      snprintf(body, sizeof(body),
        "{\"key\":\"%s\",\"temp\":%.1f,\"humidity\":%d,\"duty\":%d,\"mode\":\"%s\",\"setpoint\":%d,"
        "\"present\":%d,\"sensor\":%d,\"alarm\":%d}",
        N8N_SECRET, temp, hum, duty, modeNames[mode], (int)TEMP_ON,
        present ? 1 : 0, sensorOk ? 1 : 0, alarmState ? 1 : 0);
      code = http.POST((uint8_t*)body, strlen(body));
      if (code == 200) {
        String resp = http.getString();
        if (resp.indexOf("\"ok\":true") >= 0) {
          ok = true;
          remoteSp = jsonInt(resp, "sp");
          remoteMode = jsonInt(resp, "mode");
          remoteNew = true;      // the main loop decides what to do with it
        }
      }
      http.end();
    }
  }

  cloudOk = ok;
  if (ok != prevCloud) {
    prevCloud = ok;
    if (ok) Serial.println("n8n link: connected");
    else Serial.printf("n8n link: disconnected (code %d)\n", code);
  }
}

void syncTask(void* param) {
  unsigned long lastSyncMs = 0;
  for (;;) {
    unsigned long now = millis();
    if (syncNow || now - lastSyncMs >= SYNC_MS) {
      syncNow = false;
      lastSyncMs = now;
      syncN8n();
    }
    vTaskDelay(pdMS_TO_TICKS(200));
  }
}

// Called from loop(). Only obeys n8n when n8n's value has CHANGED,
// so your button / slider changes are not overwritten every 10 seconds.
void applyRemote() {
  if (!remoteNew) return;
  int sp = remoteSp, md = remoteMode;
  remoteNew = false;

  if (!remoteSeeded) {                 // first reply after boot: just remember it
    lastRemoteSp = sp;
    lastRemoteMode = md;
    remoteSeeded = true;
    return;
  }
  if (sp >= 22 && sp <= 35 && sp != lastRemoteSp) {
    lastRemoteSp = sp;
    applySetpoint(sp);
    Serial.printf("n8n set point: %d\n", sp);
  }
  if (md >= 0 && md <= 3 && md != lastRemoteMode) {
    lastRemoteMode = md;
    mode = (Mode)md;
    Serial.print("n8n mode: "); Serial.println(modeNames[mode]);
  }
}

// ---------- Serial / misc ----------
void printIp() {
  if (WiFi.status() == WL_CONNECTED) {
    Serial.print("Dashboard URL: http://");
    Serial.println(WiFi.localIP());
  } else Serial.println("WiFi not connected");
}

void nextMode() {
  mode = (Mode)((mode + 1) % 4);
  Serial.print("Mode changed: "); Serial.println(modeNames[mode]);
}

void handleSerial() {
  if (!Serial.available()) return;
  String s = Serial.readStringUntil('\n');
  s.trim();
  if (s.startsWith("t ")) {
    fakeTemp = s.substring(2).toFloat(); useFake = true; fakeFault = false;
  } else if (s == "r") { useFake = false; }
  else if (s == "m") { lastMotion = millis(); }
  else if (s == "b") nextMode();
  else if (s == "x") { fakeFault = !fakeFault; }
  else if (s == "i") printIp();
  else if (s == "s") { syncNow = true; }
  else if (s.startsWith("n ")) {
    String u = s.substring(2);
    u.trim();
    while (u.endsWith("/")) u.remove(u.length() - 1);
    xSemaphoreTake(n8nLock, portMAX_DELAY);
    n8nBase = u;
    xSemaphoreGive(n8nLock);
    syncNow = true;
  }
}

// ---------- Parts of the main loop ----------
void checkButton(unsigned long now) {
  bool btn = digitalRead(PIN_BTN);
  if (btn == LOW && lastBtn == HIGH && now - lastBtnMs > BTN_DEBOUNCE_MS) {
    nextMode();
    lastBtnMs = now;
  }
  lastBtn = btn;
}

void readSensor(unsigned long now) {
  if (now - lastRead < READ_MS) return;
  lastRead = now;

  if (fakeFault) {
    sensorOk = false;
  } else if (useFake) {
    temp = fakeTemp;
    sensorOk = true;
  } else {
    float t = dht.readTemperature();
    float h = dht.readHumidity();
    if (isnan(t)) {
      if (++dhtFails >= DHT_FAILS_ALLOWED) sensorOk = false;
    } else {
      temp = t;
      sensorOk = true;
      dhtFails = 0;
      if (!isnan(h)) humidity = h;
    }
  }
}

void updatePresence(unsigned long now) {
  if (now > PIR_WARMUP_MS && digitalRead(PIN_PIR) == HIGH) lastMotion = now;
  present = (now - lastMotion) < PRESENCE_HOLD_MS;
}

void updateTarget() {
  // Emergency cooling: switch the fan on when it gets dangerously hot (with a 2 degree gap before releasing)
  if (DANGER_OVERRIDES_OFF && sensorOk) {
    if (temp >= TEMP_DANGER) dangerFan = true;
    else if (temp <= TEMP_DANGER - 2) dangerFan = false;
  } else dangerFan = false;

  if (dangerFan) {
    target = 255;
  } else if (mode == OFF_MODE) {
    target = 0;
    fanOn = false;
  } else if (mode == MANUAL_ON) {
    target = MANUAL_DUTY;
  } else if (!sensorOk) {
    target = FAILSAFE_DUTY;
  } else {
    if (!fanOn && temp >= TEMP_ON) fanOn = true;
    if (fanOn && temp <= TEMP_OFF) fanOn = false;
    bool active = fanOn && (mode == AUTO_DEMO || present);
    if (active) {
      float f = constrain((temp - TEMP_ON) / (TEMP_FULL - TEMP_ON), 0.0f, 1.0f);
      target = MIN_DUTY + (int)(f * (255 - MIN_DUTY));
    } else target = 0;
  }

  if (target > 0 && prevTarget == 0) Serial.println("Fan Started");
  prevTarget = target;
}

void updateRelay(unsigned long now) {
  if (!USE_RELAY) return;
  if (target > 0 && !relayOn) {
    relayOn = true;
    relayWrite(true);
    relayMs = now;
    Serial.println("Relay closed");
  } else if (target == 0 && duty == 0 && relayOn && now - relayMs > RELAY_MIN_ON_MS) {
    relayOn = false;
    relayWrite(false);
    relayMs = now;
    Serial.println("Relay opened");
  }
}

void updateFanSpeed(unsigned long now) {
  if (now - lastRamp < RAMP_MS) return;
  lastRamp = now;

  bool relayReady = !USE_RELAY || (relayOn && now - relayMs > RELAY_SETTLE_MS);
  if (relayReady) {
    if (duty < target) duty = min(duty + RAMP_UP, target);
    else if (duty > target) duty = max(duty - RAMP_DOWN, target);
  } else {
    duty = 0;
  }

  // Inverted output (NPN driver):
  // duty 0   -> pin 255 -> fan OFF
  // duty 255 -> pin 0   -> fan FULL
  fanPwm(255 - duty);
}

void updateAlarmAndLeds(unsigned long now) {
  bool alarm = !sensorOk || temp >= TEMP_DANGER;
  if (alarm != alarmState) {
    alarmState = alarm;
    Serial.println(alarm ? "ALARM ON" : "Alarm off");
  }

  bool ledR = false, ledG = false, ledB = false;
  if (!sensorOk) { ledR = true; ledB = true; }
  else if (temp < TEMP_ON) { ledB = true; }
  else if (temp < TEMP_FULL) { ledG = true; }
  else { ledR = true; }
  if (alarmState) ledR = true;

  digitalWrite(PIN_LED_R, ledR ? HIGH : LOW);
  digitalWrite(PIN_LED_G, ledG ? HIGH : LOW);
  digitalWrite(PIN_LED_B, ledB ? HIGH : LOW);

  if (alarmState) digitalWrite(PIN_BUZZER, (now % 1000) < 200 ? HIGH : LOW);
  else digitalWrite(PIN_BUZZER, LOW);
}

void printTelemetry(unsigned long now) {
  if (now - lastPrint < 2000) return;
  lastPrint = now;
  Serial.printf("{\"temp\":%.1f,\"hum\":%.0f,\"duty\":%d,\"mode\":\"%s\",\"present\":%d,\"sensor\":%d,\"fake\":%d}\n",
                temp, isnan(humidity) ? -1.0f : humidity, duty, modeNames[mode], present, sensorOk, useFake);
}

// ---------- Setup ----------
void setup() {
  // Put the fan output in the "OFF" state as early as possible
  pinMode(PIN_FAN, OUTPUT);
  digitalWrite(PIN_FAN, HIGH);          // HIGH = fan off (inverted driver)

  Serial.begin(115200);
  Serial.setTimeout(50);

  n8nLock = xSemaphoreCreateMutex();

  pinMode(PIN_BTN, INPUT_PULLUP);
  pinMode(PIN_PIR, INPUT);
  pinMode(PIN_BUZZER, OUTPUT);  digitalWrite(PIN_BUZZER, LOW);
  pinMode(PIN_RELAY, OUTPUT);   relayWrite(false);
  pinMode(PIN_LED_R, OUTPUT);   digitalWrite(PIN_LED_R, LOW);
  pinMode(PIN_LED_G, OUTPUT);   digitalWrite(PIN_LED_G, LOW);
  pinMode(PIN_LED_B, OUTPUT);   digitalWrite(PIN_LED_B, LOW);

#if ESP_ARDUINO_VERSION_MAJOR >= 3
  ledcAttach(PIN_FAN, PWM_FREQ, 8);
#else
  ledcSetup(FAN_CHANNEL, PWM_FREQ, 8);
  ledcAttachPin(PIN_FAN, FAN_CHANNEL);
#endif
  fanPwm(255);                          // 255 = fan off

  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.setAutoReconnect(true);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("Connecting to WiFi");
  unsigned long t0 = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - t0 < 15000) {
    delay(300);
    Serial.print(".");
  }
  Serial.println();
  printIp();

  server.on("/", handleRoot);
  server.on("/status", handleStatus);
  server.on("/mode", handleMode);
  server.on("/setpoint", handleSetpoint);
  server.on("/temp", handleTemp);
  server.on("/real", handleReal);
  server.on("/motion", handleMotion);
  server.begin();

  // n8n sync runs in the background on core 0 so it can never freeze the fan
  xTaskCreatePinnedToCore(syncTask, "n8nSync", 8192, NULL, 1, NULL, 0);

  lastMotion = millis();
}

// ---------- Main loop ----------
void loop() {
  unsigned long now = millis();

  server.handleClient();
  handleSerial();

  if (WiFi.status() != WL_CONNECTED && now - lastWifi > 10000) {
    lastWifi = now;
    WiFi.reconnect();
  }

  applyRemote();
  checkButton(now);
  readSensor(now);
  updatePresence(now);
  updateTarget();
  updateRelay(now);
  updateFanSpeed(now);
  updateAlarmAndLeds(now);
  printTelemetry(now);
}
