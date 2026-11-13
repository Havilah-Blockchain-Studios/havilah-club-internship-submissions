#include <Servo.h>

int button = 2;
int buzzer = 8;
int servoPin = 9;

Servo sopuruServo; 

int lastState = HIGH;
bool triggered = false;

void setup() {
  pinMode(button, INPUT_PULLUP);
  pinMode(buzzer, OUTPUT);
  
  sopuruServo.attach(servoPin); 
  sopuruServo.write(0);         
}

void loop() {
  int currentState = digitalRead(button);

  
  if (lastState == HIGH && currentState == LOW) {
    triggered = true;
    delay(50); 
  }
  lastState = currentState;
  if (triggered) {
    
    sopuruServo.write(90);       
    digitalWrite(buzzer, HIGH);
    delay(500);              

    sopuruServo.write(0);        
    digitalWrite(buzzer, LOW);

    triggered = false; 
  }
}
