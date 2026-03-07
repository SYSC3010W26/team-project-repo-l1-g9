Weekly Individual Project Update Report

Group number: L1-G9 Student name: Chikezilim Afulukwe Week: Week 8 (Feb 28 – March 6)

How many hours did you spend on the project this week?
8 hours

Breakdown of hours spent
5 hours – Preparing and refining the end-to-end communication demo (Firebase integration and Python scripts)

3 hours – Testing system communication and validating database logging with SQLite

What did you accomplish this week? (Be specific)
This week I focused on ensuring that the communication backbone of our greenhouse monitoring system works reliably for the demonstration.

I verified the Firebase Realtime Database integration and confirmed that our nodes can successfully perform read and write operations. I tested these operations using both curl commands and Python scripts to ensure the system works across different interfaces.

I debugged several issues in the demo scripts, including incorrect Firebase paths, missing variables, and payload formatting problems. After correcting these issues, I confirmed that the scripts interact with Firebase consistently.

I validated the end-to-end communication pipeline of the system:

Node 1 publishes climate stub data to Firebase.

Node 4 retrieves the data from Firebase and logs it into a local SQLite database.

The stored entries were verified through live tail scripts and direct SQL queries.

I also implemented and tested the override control mechanism. A GUI simulation script publishes override commands to Firebase, and Node 2 polls Firebase and responds by printing actuator ON/OFF behavior, demonstrating the command flow from the user interface to the actuator layer.

Finally, I investigated intermittent SSL and network issues and confirmed stable Firebase connectivity on campus Wi-Fi. I added retry handling logic and improved the scripts to make them more reliable for the live demonstration.

How do you feel about your progress?
I feel confident about my progress this week. The communication pipeline between cloud services and local components is functioning correctly, and the data flow from Firebase to the SQLite logging system has been successfully validated. The scripts are now stable enough to support a reliable end-to-end demo.

What are you planning to do next week? (Give specific goals)
Next week I plan to:

Improve the reliability of the demo scripts by adding clearer outputs and better error handling.

Rehearse the full demonstration workflow with the team to ensure each communication link works smoothly.

Begin transitioning from stub climate data to real sensor readings once the hardware sensors are connected, while maintaining the same Firebase publish/subscribe architecture.

Is anything blocking you that you need from others?
There are no major blockers at the moment. I only need teammates to ensure they have pulled the latest repository changes and installed the required Python dependencies so the demo scripts run consistently across all devices.
