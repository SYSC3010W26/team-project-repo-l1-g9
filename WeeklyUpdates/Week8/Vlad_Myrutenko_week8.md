**1. How many hours did you spend on the project this week?**
11 Hours

**2. Give rough breakdown of hours spent on 1-3 of the following:**
*   7 Hours (Finalizing Detailed Design Sections 2 & 3)
*   2 Hours (Writing Python stubs and listeners for the Communication Demo).
*   2 Hours (Performing the demo for the TA and coordination).

**3. What did you accomplish this week? (Be specific)**
*   **Detailed Design Section 2:** Changed the Deployment Diagram to include the cooling fan (Node 1) and Arduino ADC (Node 2).
Finished the Communication Protocol Table to make sure all functional requirements were mapped to specific messages.
Created the final SQLite/NoSQL Database Schemas making sure there is support for Soil Moisture and Light Level logging.
*   **Detailed Design Section 3:** Defined the software architecture for Nodes 1-4. Created Flowcharts for the control loops of the Climate Monitor, Irrigation Manager, and Central Controller.
*   **End-to-End Demo Preparation:** Wrote and tested the Python scripts required to demonstrate the communication backbone in the lab. Specifically:
    *   `node2_poll_override.py`: Successfully demonstrated fetching commands from Firebase.
    *   `node4_firebase_to_sqlite.py`: Demonstrated the collection of Firebase Data and adding it to the local `demo_greenhouse.db`.
    *   `gui_publish_override.py`: Created a script to simulate user inputs.

**4. How do you feel about your progress?**
The work on Section 2 clarified exactly how our hardware works with the software, removing the confusion we had earlier regarding the UART vs. SPI connection for the soil sensor.
The successful execution of the demo scripts proved that our architecture is viable and ready for physical hardware integration.

**5. What are you planning to do next week? (give specific goals)**
*   Connect AHT20 sensor to Node 1 and the Relay circuit to Node 2.
*   Complete the demo scripts and add them into the final structure defined in the UML Class Diagram.

**6. Is anything blocking you that you need from others?**
None. The design is complete and the hardware components are on hand.
