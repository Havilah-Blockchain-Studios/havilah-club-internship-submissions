#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
const int redLedPin = 6;

void setup() {
  Serial.begin(9600);
  pinMode(redLedPin, OUTPUT);
  
  lcd.begin(16, 2);
  lcd.print("Sensor Ready");
  delay(2000);
  lcd.clear();
}

void loop() {
  delay(2000);

  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0) * 1000;
  float t = (voltage - 500.0) / 10.0;
  float h = 45.0 + (t - 25.0); 

  String statusMessage = "";
  if (t > 30.0) {
    statusMessage = "Too hot!";
    digitalWrite(redLedPin, HIGH);
  } else {
    statusMessage = "Nice";
    digitalWrite(redLedPin, LOW);
  }

  Serial.print("Temp: ");
  Serial.print(t);
  Serial.print(" C | Status: ");
  Serial.println(statusMessage);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.print(" C");

  lcd.setCursor(0, 1);
  lcd.print(statusMessage);
  lcd.print(" | H: ");
  lcd.print((int)h);
  lcd.print("%");
}
