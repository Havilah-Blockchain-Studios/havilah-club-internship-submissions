#include <Servo.h>
#include <NewPing.h>

// --- PIN ASSIGNMENTS (Matched to your Circuit Diagram) ---
#define SERVO_PIN 3
#define ULTRASONIC_SENSOR_TRIG 11
#define ULTRASONIC_SENSOR_ECHO 12
#define MAX_REGULAR_MOTOR_SPEED 100  // Forward speed (0-255)
#define MAX_MOTOR_ADJUST_SPEED 150   // Turning/Reversing speed (0-255)
#define DISTANCE_TO_CHECK 30         // Obstacle detection threshold in cm

// Right motor pins (L298N)
int enableRightMotor = 5;
int rightMotorPin1 = 7;
int rightMotorPin2 = 8;

// Left motor pins (L298N)
int enableLeftMotor = 6;
int leftMotorPin1 = 9;
int leftMotorPin2 = 10;

NewPing mySensor(ULTRASONIC_SENSOR_TRIG, ULTRASONIC_SENSOR_ECHO, 400);
Servo myServo;

void setup() {
  // Set motor control pins as outputs
  pinMode(enableRightMotor, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);
  
  pinMode(enableLeftMotor, OUTPUT);
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);

  // Initialize servo motor
  myServo.attach(SERVO_PIN);
  myServo.write(90); // Set servo to center position (forward)

  // Initialize Serial Monitor for debugging
  Serial.begin(9600);

  // Stop motors initially
  rotateMotor(0, 0);
}

void loop() {
  int distance = mySensor.ping_cm();

  // If sensor returns 0 (no echo/out of range), treat path as clear
  if (distance == 0) {
    distance = 100;
  }

  Serial.print("Distance: ");
  Serial.println(distance);

  // If an obstacle is detected within 30 cm
  if (distance > 0 && distance <= DISTANCE_TO_CHECK) {
    // 1. Stop motors
    rotateMotor(0, 0);
    delay(500);

    // 2. Move backward briefly
    rotateMotor(-MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED);
    delay(300);

    // 3. Stop motors before scanning
    rotateMotor(0, 0);
    delay(300);

    // 4. Look right and left to check clearances
    int distanceRight = lookRight();
    int distanceLeft = lookLeft();
    delay(300);

    // 5. Compare distances and turn toward the clearer path
    if (distanceRight > distanceLeft) {
      // Turn right (Right motor reverse, Left motor forward)
      rotateMotor(MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED);
    } else {
      // Turn left (Right motor forward, Left motor reverse)
      rotateMotor(-MAX_MOTOR_ADJUST_SPEED, MAX_MOTOR_ADJUST_SPEED);
    }
    delay(400); // Adjust turn duration if necessary

    // 6. Stop briefly before resuming loop
    rotateMotor(0, 0);
    delay(200);
  } 
  else {
    // Move forward normally
    rotateMotor(MAX_REGULAR_MOTOR_SPEED, MAX_REGULAR_MOTOR_SPEED);
  }

  delay(50);
}

// Function to look right and return distance
int lookRight() {
  myServo.write(0); // 0 degrees = Right
  delay(500);
  int d = mySensor.ping_cm();
  if (d == 0) d = 100;
  myServo.write(90); // Reset to center
  delay(300);
  return d;
}

// Function to look left and return distance
int lookLeft() {
  myServo.write(180); // 180 degrees = Left
  delay(500);
  int d = mySensor.ping_cm();
  if (d == 0) d = 100;
  myServo.write(90); // Reset to center
  delay(300);
  return d;
}

// Motor control function using PWM speeds (Positive = Forward, Negative = Reverse)
void rotateMotor(int rightMotorSpeed, int leftMotorSpeed) {
  if (rightMotorSpeed < 0) {
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, HIGH);    
  } else {
    digitalWrite(rightMotorPin1, HIGH);
    digitalWrite(rightMotorPin2, LOW);      
  }

  if (leftMotorSpeed < 0) {
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, HIGH);    
  } else {
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);      
  }

  analogWrite(enableRightMotor, abs(rightMotorSpeed));
  analogWrite(enableLeftMotor, abs(leftMotorSpeed));    
}
