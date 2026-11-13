#include <Servo.h>

Servo myServo;
const int pingPin = 7;
const int redLedPin = 8;
const int greenLedPin = 12;
const int buzzerPin = 5;

bool doorIsOpen = false; // Tracks door state so buzzer only beeps once when opening

void setup() {
  Serial.begin(9600);
  myServo.attach(6);
  pinMode(redLedPin, OUTPUT);
  pinMode(greenLedPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  long cm = readDistanceCm();

  if (cm > 0 && cm < 20) {
    // If door was previously closed, beep once as it opens
    if (!doorIsOpen) {
      tone(buzzerPin, 1000, 150); // 1000 Hz tone for 150ms
      doorIsOpen = true;
    }

    myServo.write(90);
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(redLedPin, LOW);
  } else {
    doorIsOpen = false; // Reset door status when closed
    myServo.write(0);
    digitalWrite(greenLedPin, LOW);
    digitalWrite(redLedPin, HIGH);
  }

  delay(100);
}

long readDistanceCm() {
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  pinMode(pingPin, INPUT);
  long duration = pulseIn(pingPin, HIGH);
  
  return duration / 29 / 2;
}
