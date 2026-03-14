# Weekly Individual Project Update Report

- **Group number:** L1-G9
- **Student name:** Vlad Myrutenko
- **Week:** Week 9

### 1. How many hours did you spend on the project this week?
2 Hours

### 2. Give rough breakdown of hours spent on 1-3 of the following:
*   **2 Hours:** Writing and automating standalone unit tests for hardware and software components to prepare for the Unit Test Demo.

### 3. What did you accomplish this week? (Be specific).
*   Drafted the isolated unit test scripts for the AHT20 Sensor (verifying I2C communication and stable temperature/humidity reading ranges) and the Relay + Pump control (toggling GPIO to confirm the relay safely energizes/de-energizes).
*   Drafted an automated software unit test for the **Threshold Logic** to verify that the system correctly evaluates simulated soil moisture inputs (e.g., triggering the pump `ON` when below 30% and `OFF` when above).

### 4. How do you feel about your progress?
It was a lighter week for me in terms of hours, but I feel good about where we stand. Because Karthikeyan successfully stabilized the communication pipeline and manual overrides, 
setting up these isolated unit tests was straightforward. We now have a solid foundation to verify our individual modules before we merge the hardware and software together.

### 5. What are you planning to do next week? (give specific goals)
*   Run my drafted unit tests on the actual physical hardware (connecting the AHT20 to Node 1 and the Relay circuit to Node 2), replacing the stub values with real readings.
*   Upload the finalized, automated test programs to our project GitHub repository before our lab.
*   Rehearse my portion of the Unit Test demo to ensure I can successfully demonstrate at least two tests (one hardware, one software) to the TA.

### 6. Is anything blocking you that you need from others?
Just coordinating with the team to ensure our Raspberry Pi environments (Python venvs, required libraries) are identical. 
Like Karthikeyan mentioned, we need to make sure the Pi connects reliably to the campus Wi-Fi so our scripts and tests run deterministically during the live demo.
I am also dependent on the final hardware assembly being completed so I can run the physical hardware unit tests.
