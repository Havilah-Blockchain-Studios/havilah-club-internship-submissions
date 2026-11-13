# Obstacle-Avoiding Autonomous Robotic Car

## One-Line Description
ObstacleBot is an autonomous microcontroller-driven robotic vehicle that helps navigate unknown indoor environments by detecting obstacles in real-time, scanning alternate pathways, and executing collision-avoidance maneuvers.

## Problem Statement
Manual or pre-programmed mobile robots frequently collide with physical barriers, get trapped in confined dead-ends, and lack intelligent environmental feedback when navigating unstructured spaces.

## Solution
An Arduino-powered smart robotic car integrating ultrasonic distance sensing, mechanical environmental scanning via a servo motor, and custom C++ navigation logic that handles obstacle evasion and 180° dead-end escapes.

## Full Components List
- Arduino Uno R3 Microcontroller
- L298N Dual H-Bridge Motor Driver Module
- 4x TT DC Gear Motors with Wheels
- HC-SR04 Ultrasonic Distance Sensor
- TowerPro SG90 Micro Servo Motor
- Toggle Switch & 18650 Lithium-ion Battery Pack
- Breadboard & Jumper Wires (Red and Black)

## Step-by-Step Setup Instructions
1. **Chassis Assembly:** Mount the 4 TT motors onto the acrylic chassis and attach the caster wheel and tires.
2. **Power Wiring:** Connect the battery pack through the slide switch to the L298N power terminals (`12V`, `GND`). Run a regulated `5V` jumper line from the L298N to the Arduino Uno.
3. **Motor Connections:** Wire the DC gear motors to the L298N output channels (`OUT1`–`OUT4`) and connect control pins to Arduino digital pins.
4. **Sensor Integration:** Mount the HC-SR04 sensor onto the SG90 servo horn. Connect Trigger and Echo pins to designated Arduino digital pins, and power the servo/sensor via the 5V rail with a common ground.
5. **Firmware Upload:** Connect the Arduino Uno to your PC via USB Cable, Arduino IDE, compile, and upload the C++ navigation code.

## How to Run It
1. Turn on the Toggle switch to power the system from the battery pack.
2. Place the robot on a flat test track or enclosed floor area.
3. The robot will drive forward autonomously, scan ahead using the ultrasonic sensor, and avoid obstacles or execute a 180° turn upon entering a dead-end.
