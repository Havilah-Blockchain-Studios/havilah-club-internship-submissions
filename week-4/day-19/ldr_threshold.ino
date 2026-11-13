int greenLed = 13;

void setup() {
  Serial.begin(9600);
  pinMode(greenLed, OUTPUT);
}

void loop() {
  int value = analogRead(A0);
  Serial.println(value);

  // Turn ON when light drops below 
  if (value < 300) {
    digitalWrite(greenLed, HIGH);
  } 
  // Turn OFF when light rises above 400 
  else if (value > 400) {
    digitalWrite(greenLed, LOW);
  }

  delay(500);
}
