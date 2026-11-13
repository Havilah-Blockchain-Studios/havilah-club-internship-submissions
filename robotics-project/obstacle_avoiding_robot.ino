#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <Dabble.h>
#include <Servo.h>
#include <NewPing.h>

// --- PIN ASSIGNMENTS (Matched to your Circuit Diagram) ---
#define SERVO_PIN 3
#define ULTRASONIC_SENSOR_TRIG 11
#define ULTRASONIC_SENSOR_ECHO 12

// --- SPEED & THRESHOLD SETTINGS ---
#define MAX_REGULAR_MOTOR_SPEED 100   // Forward cruise speed (0-255)
#define MAX_MOTOR_ADJUST_SPEED 160    // Standard turning/reversing speed (0-255)
#define U_TURN_MOTOR_SPEED 250        // High-torque speed for 180° spin (0-255)
#define DISTANCE_TO_CHECK 30          // Obstacle detection threshold in cm

// --- PHYSICAL CALIBRATION ---
#define TURN_180_DURATION 1100        // Time in ms for exact 180° turn

// Right motor pins (L298N)
const int enableRightMotor = 5;
const int rightMotorPin1 = 7;
const int rightMotorPin2 = 8;

// Left motor pins (L298N)
const int enableLeftMotor = 6;
const int leftMotorPin1 = 9;
const int leftMotorPin2 = 10;

NewPing mySensor(ULTRASONIC_SENSOR_TRIG, ULTRASONIC_SENSOR_ECHO, 400);
Servo myServo;

// Robot operating modes
enum RobotMode {
  WAITING_FOR_CONNECTION, // Startup state: waits for Bluetooth connection & Start button
  AUTONOMOUS_MODE,        // Autonomous obstacle avoidance & 180° escapes
  MANUAL_MODE             // Teleoperation via Dabble Gamepad arrows
};

RobotMode currentMode = WAITING_FOR_CONNECTION;
bool isMovingForward = false;

// Function declarations
void rotateMotor(int rightMotorSpeed, int leftMotorSpeed);
void executeUTurn180();
int lookRight();
int lookLeft();
void runAutonomousRoutine();

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
  myServo.write(90); // Center position (facing forward)

  // Initialize Serial Monitor and Dabble Bluetooth
  Serial.begin(9600);
  Dabble.begin(9600); 

  // Ensure motors start completely stopped
  rotateMotor(0, 0);
  
  Serial.println("----------------------------------------");
  waitingScreenMessage();
}

void loop() {
  // 1. Always process incoming Bluetooth data from Dabble
  Dabble.processInput(); 

  // 2. Global Mode Switching Buttons
  if (GamePad.isSelectPressed()) {
    currentMode = WAITING_FOR_CONNECTION;
    rotateMotor(0, 0);
    myServo.write(90);
    isMovingForward = false;
    Serial.println(">>> SYSTEM PAUSED: Returned to Waiting/Standby Mode.");
  } 
  else if (GamePad.isStartPressed()) {
    currentMode = AUTONOMOUS_MODE;
    Serial.println(">>> START PRESSED: Entering Autonomous Mode!");
  }

  // 3. Manual Override: If any directional arrow is pressed, switch to Manual Mode
  if (GamePad.isUpPressed()) {
    currentMode = MANUAL_MODE;
    isMovingForward = false;
    rotateMotor(MAX_REGULAR_MOTOR_SPEED, MAX_REGULAR_MOTOR_SPEED); // Drive forward manually
  }
  else if (GamePad.isDownPressed()) {
    currentMode = MANUAL_MODE;
    isMovingForward = false;
    rotateMotor(-MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED); // Drive backward (Call it back!)
  }
  else if (GamePad.isLeftPressed()) {
    currentMode = MANUAL_MODE;
    isMovingForward = false;
    rotateMotor(-MAX_MOTOR_ADJUST_SPEED, MAX_MOTOR_ADJUST_SPEED); // Turn/Spin left
  }
  else if (GamePad.isRightPressed()) {
    currentMode = MANUAL_MODE;
    isMovingForward = false;
    rotateMotor(MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED); // Turn/Spin right
  }
  else {
    // If we were in manual mode but released all keys, stop the motors
    if (currentMode == MANUAL_MODE) {
      if (!GamePad.isUpPressed() && !GamePad.isDownPressed() && !GamePad.isLeftPressed() && !GamePad.isRightPressed()) {
        rotateMotor(0, 0);
      }
    }
  }

  // 4. Handle Behavior Based on Current Mode
  switch (currentMode) {
    case WAITING_FOR_CONNECTION:
      rotateMotor(0, 0); // Keep motors locked until activated
      myServo.write(90);
      delay(100);
      break;

    case MANUAL_MODE:
      // Handled dynamically by the arrow key listeners above
      delay(20);
      break;

    case AUTONOMOUS_MODE:
      runAutonomousRoutine();
      break;
  }
}

// --- AUTONOMOUS OBSTACLE AVOIDANCE ROUTINE ---
void runAutonomousRoutine() {
  int distance = mySensor.ping_cm();

  if (distance == 0) {
    distance = 100; // Out of range = clear path
  }

  Serial.print("Autonomous Distance: ");
  Serial.println(distance);

  if (distance > 0 && distance <= DISTANCE_TO_CHECK) {
    isMovingForward = false;

    // Full stop
    rotateMotor(0, 0);
    delay(300);

    // Back up to create clearance
    rotateMotor(-MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED);
    delay(500);

    // Stop before scanning
    rotateMotor(0, 0);
    delay(300);

    // Scan sides
    int distanceRight = lookRight();
    int distanceLeft = lookLeft();
    delay(200);

    // Dead end / 180 check
    if (distanceRight <= DISTANCE_TO_CHECK && distanceLeft <= DISTANCE_TO_CHECK) {
      Serial.println("DEAD END! Executing 180° U-Turn...");
      executeUTurn180();
    } 
    else if (distanceRight > distanceLeft) {
      rotateMotor(MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED);
      delay(550);
    } 
    else {
      rotateMotor(-MAX_MOTOR_ADJUST_SPEED, MAX_MOTOR_ADJUST_SPEED);
      delay(550);
    }

    rotateMotor(0, 0);
    delay(200);
  } 
  else {
    if (!isMovingForward) {
      rotateMotor(MAX_REGULAR_MOTOR_SPEED, MAX_REGULAR_MOTOR_SPEED);
      isMovingForward = true;
    }
  }

  delay(50);
}

// --- HELPER FUNCTIONS ---

void waitingScreenMessage() {
  Serial.println("Robot is in WAITING/STANDBY state.");
  Serial.println("1. Connect via Dabble app.");
  Serial.println("2. Press [START] to begin Autonomous Mode.");
  Serial.println("3. Use Arrow Keys to drive manually (Call back / Maneuver).");
  Serial.println("----------------------------------------");
}

void executeUTurn180() {
  rotateMotor(-MAX_MOTOR_ADJUST_SPEED, -MAX_MOTOR_ADJUST_SPEED);
  delay(400);
  
  rotateMotor(0, 0);
  delay(200);

  rotateMotor(U_TURN_MOTOR_SPEED, -U_TURN_MOTOR_SPEED);
  delay(TURN_180_DURATION);

  rotateMotor(0, 0);
  delay(300);
}

int lookRight() {
  myServo.write(0);
  delay(400);
  int d = mySensor.ping_cm();
  if (d == 0) d = 100;
  myServo.write(90);
  delay(200);
  return d;
}

int lookLeft() {
  myServo.write(180);
  delay(400);
  int d = mySensor.ping_cm();
  if (d == 0) d = 100;
  myServo.write(90);
  delay(200);
  return d;
}

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
