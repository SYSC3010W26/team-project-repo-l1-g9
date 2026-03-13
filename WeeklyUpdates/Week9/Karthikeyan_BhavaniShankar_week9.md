Weekly Individual Project Update Report

- Group number: L1-G9
- Student name: Karthikeyan Bhavani Shankar
- Week: March 5–8, 2026

1) How many hours did you spend on the project this week?

- 8 hours

2) Breakdown of hours spent:

- Top item: Communications demo implementation + debugging (Firebase ↔ Node scripts) – 5 hours

- 2nd item: Documentation updates (protocol table, test plan evidence, flowchart/diagrams integration) – 3 hours

3) What did you accomplish this week?

- Implemented and validated the end-to-end communications demo pipeline: Node1 → Firebase RTDB → Node4 → SQLite, including a SQLite “tail viewer” script to show live database updates as proof during the demo.

- Implemented and validated the manual override command flow: GUI publisher → Firebase /commands/override → Node2 receiver, where Node2 correctly prints and applies ON/OFF actuation states.

- Debugged key integration issues, including:

- Resolving Firebase overwrite vs history logging (switching telemetry publishing from PUT-style overwrite to POST with push IDs where needed).

- Fixing schema/path mismatches between Node1 publishing paths and Node4 logging paths (ensuring both use the same RTDB path).

- Ensuring all demo scripts run with finite loop counts (e.g., 10 iterations) to avoid infinite runs during the demo.

- Coordinated demo readiness by confirming a consistent terminal/role split across teammates (Node1 publisher, Node4 logger, SQLite proof viewer, override publisher, Node2 receiver).

4) How do you feel about your progress?

- I feel confident about the communication links demonstrated so far because we now have repeatable terminal outputs and Firebase/SQLite evidence that clearly proves the system pipeline.

- The system is in a good place for the comms demo since the scripts run deterministically (finite iterations) and the database paths are standardized, reducing integration risk during the live demo.

5) What are you planning to do next week?

- Replace stub sensor values with real hardware readings where available (AHT20 and soil moisture via Arduino/ADC) and confirm calibration ranges.

- Expand Node4 logging to include additional fields (soil moisture, light level) as those nodes come online, and finalize database schema tables in the report.

- Finalize documentation polish: communication protocol table (2.2.1), database schema (2.4), and clean figure captions + diagram references.

6) Is anything blocking you that you need from others?

- Main blocker is ensuring all teammates have a consistent environment setup (Python venv + required libraries) and that each Raspberry Pi is configured to run the assigned demo script reliably on campus Wi-Fi.

- Hardware availability (sensors/actuators fully wired) may limit how much of the demo can use real readings vs stub data this week.
