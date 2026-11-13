// variable declaration
int buttonPin = 2;   
int motorPin = 5;    
int relayPin = 4;  
int potPin = A0;     

bool motorState = false;        
bool lampState = false;
int lastButtonState = HIGH;     

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); 
  pinMode(motorPin, OUTPUT);
  pinMode(relayPin, OUTPUT);
  pinMode(potPin, INPUT);
  
  digitalWrite(motorPin, LOW);
  digitalWrite(relayPin, LOW);
  Serial.begin(9600);
}

void loop() {
  
  int reading = digitalRead(buttonPin);
  if (reading != lastButtonState) {
    delay(50);
  }

 
  if (reading == LOW && lastButtonState == HIGH) {
    motorState = !motorState;
    lampState = !lampState; 
    
    if (motorState) {
      Serial.println("Motor & Lamp ON");
    } else {
      Serial.println("Motor & Lamp OFF");
    }
  }

  
  lastButtonState = reading;

  
  if (lampState) {
    digitalWrite(relayPin, HIGH);
  } else {
    digitalWrite(relayPin, LOW);
  }

  
  if (motorState) {
    int potValue = analogRead(potPin); 
    int motorSpeed = map(potValue, 0, 1023, 0, 255);
    int speedPercent = map(potValue, 0, 1023, 0, 100);

    analogWrite(motorPin, motorSpeed);

    Serial.print("Motor Speed: ");
    Serial.print(speedPercent);
    Serial.println("%");
    
    delay(200); 
  } else {
    digitalWrite(motorPin, LOW);
  }
}
