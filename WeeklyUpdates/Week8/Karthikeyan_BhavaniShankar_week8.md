Weekly Individual Project Update Report

- Group number: L1-G9
- Student name: Karthikeyan Bhavani Shankar
- Week: Week 6(Feb 25th – Feb 28th)

1) How many hours did you spend on the project this week?
7 hours

2) Breakdown of hours spent:
- Top item: End-to-end communications demo setup and debugging (Firebase + scripts) – 4 hours
- 2nd item: Testing, validation, and documentation updates (README + demo steps) – 3 hours

3) What did you accomplish this week? 

- Set up and verified Firebase Realtime Database access for our demo environment and confirmed read/write functionality using both curl and Python scripts.

- Debugged and corrected demo scripts to ensure consistent Firebase paths and proper request behavior (including resolving issues such as missing variables like PATH and payload formatting problems).

- Validated the end-to-end data pipeline: Node1 publishes climate stub data to Firebase, Node4 reads from Firebase and logs it into SQLite, and SQLite entries are verified using live tail scripts and direct SQL queries.

- Implemented and tested the bidirectional override link: the GUI script publishes override commands to Firebase, and Node2 polls Firebase and prints actuator ON/OFF behavior automatically.

- Investigated intermittent SSL/network issues and confirmed Firebase connectivity on campus Wi-Fi; prepared reliability improvements (retry handling) to prevent demo scripts from crashing during the live demonstration.

- Updated the demo workflow notes so the team can run scripts in the correct order during the Thursday communications demo.

4) How do you feel about your progress?
I feel confident about the progress this week. The core communication links required for the demo are working and repeatable, and the data flow from cloud to local logging is clearly demonstrated. The demo steps are now structured so that each team member can reliably show their communication link.

5) What are you planning to do next week?

- Finalize the communication protocol table to match the deployment diagram and demo scripts.

- Add small improvements for demo reliability (retries, clearer printed outputs, and consistent Firebase endpoints) and rehearse the full demo flow with the team.

- Begin transitioning from stub sensor data to real sensor readings once hardware is available, while keeping the same publish/subscribe architecture.

6) Is anything blocking you that you need from others?
   
- No major blockers. I need teammates to pull the latest repository changes and ensure their Python environment is set up so the demo scripts run consistently on their devices.
