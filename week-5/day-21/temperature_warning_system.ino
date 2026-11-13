int tempSensor = A1;
int redLed = 9;
int greenLed = 8;
int pushButton = 2;
int buzzerPin = 7;

bool armed = false;
bool alarmTriggered = false;
int lastButtonState = HIGH;

void setup() {
  pinMode(tempSensor, INPUT);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(pushButton, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(pushButton);
  if (buttonState == LOW && lastButtonState == HIGH) {
    if (armed) {
      armed = false;
      alarmTriggered = false;
    } else {
      armed = true;
    }
    delay(50);
  }
  lastButtonState = buttonState;

  int reading = analogRead(tempSensor);
  float voltage = reading * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100.0;

  if (armed && temperature > 30.0) {
    alarmTriggered = true;
  }

  if (armed) {
    if (alarmTriggered) {
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
      tone(buzzerPin, 1200, 200);
    } else {
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
      noTone(buzzerPin);
    }
  } else {
    digitalWrite(greenLed, LOW);
    digitalWrite(redLed, LOW);
    noTone(buzzerPin);
    alarmTriggered = false;
  }

  Serial.print("Temp: ");
  Serial.println(temperature);
  delay(100);
}
