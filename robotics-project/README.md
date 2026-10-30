Smart Robotic Car - Group 3 (Havilah Blockchain Studios)

Overview
An autonomous obstacle-avoiding robotic car built using an Arduino Uno microcontroller, L298N dual H-bridge motor driver, 4 TT gear motors, and an HC-SR04 ultrasonic distance sensor.

Hardware Components
- Arduino Uno R3
- L298N Motor Driver Module
- 4x TT Gear Motors & Wheels
- HC-SR04 Ultrasonic Sensor
- SG90 Servo Motor
- Custom Power Assembly & Multimeter Tested Wiring

System Architecture & Functionality
- **Happy Path:** Navigates forward until an obstacle is detected within threshold range.
- **Obstacle Avoidance:** Halts motor direction via L298N driver upon distance detection.
- **Power Management:** Custom battery holder contacts stabilized and verified using a multimeter to prevent voltage drops.
