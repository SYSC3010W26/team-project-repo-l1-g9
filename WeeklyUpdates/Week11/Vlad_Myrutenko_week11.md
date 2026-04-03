Weekly Individual Project Update Report

# Weekly Individual Project Update Report

- **Group number:** L1-G9
- **Student name:** Vlad Myrutenko
- **Week:** Week 11

### 1. How many hours did you spend on the project this week?
10 Hours

### 2. Give rough breakdown of hours spent on 1-3 of the following:
*   **4 Hours:** Filming, coordinating, and executing the Final Video Demo (recording my solo hardware explanation and participating in the live Discord synchronized demo).
*   **4 Hours:** Finalizing the physical hardware build for Node 2 (wiring the Arduino, soil moisture sensor, and 12V pump via the active-low relay) and debugging the Python/UART integration.
*   **2 Hours:** Rehearsing the script, preparing the physical props (plant/water), and coordinating the plan for the live In-Lab Final Demo.

### 3. What did you accomplish this week? (Be specific).
*   Successfully assembled and tested the final physical hardware for Node 2. I integrated the Arduino Uno to act as an ADC coprocessor, successfully reading the capacitive soil moisture sensor and passing that data to the Raspberry Pi via USB UART.
*   Wired the 12V peristaltic pump to the 2-channel 5V relay module, successfully adapting my Python script to handle the module's "Active-Low" logic for safe actuation.
*   Recorded my 2-minute solo segment for the Final Video Demo, detailing our communication protocols (UART, HTTPS/REST) and demonstrating the automatic irrigation loop.
*   Participated in the live, synchronized Discord recording where we successfully proved our remote IoT capabilities (Karth clicking the GUI override on his screen, which instantly triggered my physical pump over Firebase).
*   Prepped all physical props and finalized my speaking points for the live in-lab Final Demo acceptance testing.

### 4. How do you feel about your progress?
I feel incredibly proud and relieved. Moving from software stubs to actual, clicking relays and pumping water was a massive step.
Seeing the physical hardware actuate perfectly based on both local sensor thresholds and remote cloud commands during our video recording was a huge payoff. We are 100% prepared for the final lab demo.

### 5. What are you planning to do next week? (give specific goals)
*   Successfully deliver the live 20-minute Final Demo in the lab alongside my team, ensuring my Node 2 hardware performs flawlessly during the acceptance testing.
*   Write and finalize my assigned sections for the Final Project Report (specifically detailing the Node 2 hybrid controller design, the Arduino UART integration, and my personal reflections).
*   Help review and clean up our GitHub repository, ensuring the README is properly formatted and the codebase is completely frozen before the final submission deadline.

### 6. Is anything blocking you that you need from others?
No blockers at this time. The only potential risk is campus Wi-Fi instability during the live demo, but we have already coordinated a mobile hotspot fallback plan to ensure our nodes can securely reach Firebase without interruption.
