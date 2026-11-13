int redLed = 13; 

void setup() {
  pinMode(redLed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(redLed, HIGH);
  Serial.println("LED ON");    
  delay(1000);                 
  
  digitalWrite(redLed, LOW);
  Serial.println("LED OFF");
  delay(1000);                 
}
