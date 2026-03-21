# Weekly Individual Project Update Report

- **Group number:** L1-G9
- **Student name:** Vlad Myrutenko
- **Week:** Week 10

### 1. How many hours did you spend on the project this week?
8 Hours

### 2. Give rough breakdown of hours spent on 1-3 of the following:
*   **4 Hours:** Preparing, adapting, and executing the Unit Test Demo.
*   **4 Hours:** Finalizing the physical hardware requirements, calculating voltage/amperage safety margins, and ordering the final physical components.

### 3. What did you accomplish this week? (Be specific).
*   Successfully delivered the Unit Test Demo. Because we were missing some physical sensors and an Arduino, I helped the team pivot to using the Pi's SenseHAT and software stubs to successfully prove our threshold logic and automated tests to the TA.
*   Finalized the complete hardware list and purchased all the required physical components for the final build (Arduino Uno, 12V peristaltic dosing pump, 12V cooling fan, 5V opto-isolated relay modules, capacitive soil sensors, and tubing).
*   Verified the power draw math (e.g., ensuring our 12V 2A power supply can safely handle both the fan and the pump simultaneously without browning out the system).

### 4. How do you feel about your progress?
I feel very confident. We survived a stressful Unit Test Demo by adapting our software to simulate the missing hardware, which proved our architecture is solid.
Now that the correct, voltage-matched physical parts are officially ordered and arriving Monday, we are perfectly positioned to build the real system.

### 5. What are you planning to do next week? (give specific goals)
*   Receive the hardware order on Monday and immediately begin physical assembly.
*   Flash the Arduino Uno with the C++ ADC code so it can read the analog soil moisture sensors.
*   Wire the 12V power supply to the relay modules and connect the physical pump and fan.
*   Work with the team to replace our software stubs with the real hardware integration scripts.

### 6. Is anything blocking you that you need from others?
I am just waiting on the hardware delivery arriving on Monday. Once the parts are in hand, I will be building the circuits and will need the team to be ready to help test the final Python scripts with the physical GPIO pins.
