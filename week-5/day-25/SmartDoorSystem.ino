#include <Servo.h>

// Global Declaration
const int pingPin = 7;
const int redLed = 8;
const int greenLed = 12;
const int buzzer = 5;
const int button = 2;

Servo sopuruServo;

// State Variables
bool isLocked = false;
bool doorIsOpen = false; 

void setup() {
  sopuruServo.attach(6);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(button, INPUT_PULLUP);
}

void loop() {
// 1. Toggle Lock Mode via Button Press
if (digitalRead(button) == LOW) {
    isLocked = !isLocked;        
    tone(buzzer, 800, 200);      
    delay(300);                 
}

// 2. Manual Lockdown Mode
if (isLocked) {
    setDoorState(false, 0);
} 
// 3. Proximity Entry Mode
else {
    long cm = readDistance();
    
  if (cm > 0 && cm < 20) {
    if (!doorIsOpen) {
      tone(buzzer, 1000, 150); // Single transition beep
      doorIsOpen = true;
}
      setDoorState(true, 95);    // Open door
} else {
      doorIsOpen = false;        // Reset when object moves away
      setDoorState(false, 0);    // Close door
  }
 }
  
  delay(100);
}

// Helper function to control door state and LEDs
void setDoorState(bool open, int angle) {
  sopuruServo.write(angle);
  digitalWrite(greenLed, open ? HIGH : LOW);
  digitalWrite(redLed, open ? LOW : HIGH);
}

// Function to measure distance using the ultrasonic sensor
long readDistance() {
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);
  
  pinMode(pingPin, INPUT);
  return pulseIn(pingPin, HIGH) / 29 / 2;
}
