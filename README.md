# SYSC3010 Automated Greenhouse Monitoring and Irrigation System

**Group L1-G9**
* Esteban Heidrich
* Vlad Myrutenko
* Karthikeyan Bhavani Shankar
* Chikezilim Afulukwe

**TA:** Gabriel Seyoum | **Course:** SYSC 3010

## Project Summary
This project is a distributed, Internet of Things (IoT) automated greenhouse system. It utilizes four independent Raspberry Pi edge nodes that communicate asynchronously via a Firebase Realtime Database. The system is designed to reduce the manual labor of greenhouse farming by continuously monitoring temperature, humidity, soil moisture, and light levels. Node 1 controls a 12V cooling fan based on temperature thresholds. Node 2 utilizes an Arduino coprocessor to monitor soil moisture and controls a 12V peristaltic irrigation pump. Node 3 monitors plant health via a camera. Finally, Node 4 acts as the central data historian, logging all cloud telemetry into a local SQLite database and hosting a Web GUI that allows users to view live charts and issue remote manual override commands to the actuators.

## Repository Directory Structure
* `/implementation/` - Contains the core operational Python scripts for all four nodes (`node1_climate.py`, `node2_irrigation.py`, `node3_camera.py`, `node4_logger.py`), along with SenseHat fallback scripts and the local `greenhouse.db` SQLite database.
* `/gui/` - Contains the frontend dashboard files (`index.html`, `script.js`, `style.css`) used to monitor live system telemetry and send manual overrides.
* `/unittest/` - Contains our automated software testing suite (`test_software_logic.py`) and isolated hardware verification scripts (`test_hw_actuator.py`, `test_hw_camera.py`, `test_hw_climate.py`).
* `/demo_tests/` - Contains early communication integration scripts, environment setup files, and our `requirements.txt`.
* `/WeeklyUpdates/` - Contains the Markdown files for each team member's Weekly Individual Project Update Reports (WIPURs).

## Installation Instructions
1. Clone this repository to your Raspberry Pi nodes.
2. Ensure Python 3 is installed on your system.
3. Install the required dependencies by navigating to the repository root and running:
   `pip3 install -r demo_tests/requirements.txt` 
   *(This installs `requests`, `pyserial`, `smbus2`, `sense_hat`, and `RPi.GPIO`).*
4. **Firebase Configuration:** Update the `FIREBASE_URL` variable inside the node scripts to point to your specific Firebase instance. Ensure your Firebase Realtime Database rules are set to allow read/write access.
5. **Hardware Prep (Node 2):** Flash the Arduino Uno with the C++ analog read sketch to act as the ADC, and connect it to Node 2 via USB.

## How to Run the System
The system is fully distributed and the nodes can be started in any order. Open a terminal on the respective Raspberry Pis and execute the following from the repository root:

* **Node 1 (Climate):** `python3 implementation/node1_climate.py`
* **Node 2 (Irrigation):** `python3 implementation/node2_irrigation.py`
* **Node 3 (Health):** `python3 implementation/node3_camera.py`
* **Node 4 (Logger):** `python3 implementation/node4_logger.py`

**To launch the Web GUI:**
1. Navigate into the GUI folder: `cd gui`
2. Start a local Python web server: `python -m http.server 8000`
3. Open a web browser and navigate to: `http://localhost:8000`

## Verification (How to know it is working)
* **Software Tests:** Navigate to the `/unittest/` folder and run `python3 test_software_logic.py`. The console should report `OK` indicating the irrigation threshold logic, payload formatting, and SQLite database operations are functioning correctly.
* **Terminal Output:** Once the node scripts are running, you will see periodic terminal printouts displaying sensor readings and actuator states (e.g., `AUTO LOGIC -> Pump: ON`).
* **Database Logging:** Node 4's terminal will print confirmation messages as it successfully fetches Firebase data and inserts it into `greenhouse.db`.
* **Actuation Check:** Remove the soil sensor from the dirt on Node 2; the physical water pump will click on. Submerge it in water, and the pump will turn off.
* **Remote Override Check:** Open the Web GUI and click the "Manual Override Pump ON" button. Within 1-2 seconds, Node 2's terminal will display `OVERRIDE ACTIVE` and the physical pump will turn on, proving the end-to-end cloud command pathway is active.
