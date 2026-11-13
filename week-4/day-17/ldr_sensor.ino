int ldrPin = A0;
int redPin = 13;
int threshold = 500; 

void setup() {
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(ldrPin, INPUT);
}

void loop() {
  int ldrValue = analogRead(ldrPin);
  Serial.println(ldrValue);

  if (ldrValue < threshold) {
    digitalWrite(redPin, LOW); 
  } else {
    digitalWrite(redPin, HIGH);  
  }
  
  delay(500);
}
