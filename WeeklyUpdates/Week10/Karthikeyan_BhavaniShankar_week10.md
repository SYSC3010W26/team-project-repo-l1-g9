Weekly Individual Project Update Report

- Group number: L1-G9
- Student name: Karthikeyan Bhavani Shankar
- Week: Week 7(March 5th - March 8th)

1) How many hours did you spend on the project this week?

-  9 hours

2) Breakdown of hours spent:
   
-  Top item: Communication demo testing and debugging (Firebase RTDB, Node scripts, SQLite logging) – 5 hours

-  2nd item: Detailed design document updates and unit test preparation – 4 hours

3) What did you accomplish this week?

- Completed and validated the main communication demo flow for the project:

- Node1 → Firebase → Node4 → SQLite

- GUI → Firebase → Node2

- Verified that climate data can be published to Firebase from Node1 and successfully logged into the local SQLite database by Node4.

- Confirmed that the SQLite “tail viewer” can be used as proof that data is being inserted continuously into the local database.

- Tested the manual override communication path, where a GUI publisher sends pump_enable commands to Firebase and Node2 receives them and maps them to ON/OFF actuator decisions.

- Helped debug communication issues related to Firebase path consistency, POST vs PUT behavior, and mixed data formats in the database.

- Updated and refined major sections of the Detailed Design report, including:

-- communication protocols,

-- database schema,

-- software design sections for the four nodes,

-- test plan sections,

-- figure captions and activity diagram descriptions.

- Began preparing for the unit test demo by identifying which existing software/database tests are already complete and which dedicated hardware tests still need to be added.

4) How do you feel about your progress?

- I feel good about the progress this week because the project now has a working communication backbone that we can demonstrate clearly. The main software links are behaving consistently, and we also have stronger report documentation than before. I think the next important step is shifting more attention from communication scripts to isolated hardware unit tests so we are ready for Friday’s rubric.

5) What are you planning to do next week?

- Prepare and run dedicated hardware unit tests for the major components, including the AHT20 sensor, relay/pump path, and fan control path.

- Make sure all test programs are uploaded to GitHub before the unit test demo.

- Continue integrating real hardware readings where available instead of stub/demo values.

- Finalize any remaining sections of the detailed design report and make sure the implementation matches the documentation.

6) Is anything blocking you that you need from others?

The biggest dependency right now is making sure all teammates finish and verify their assigned hardware-side unit tests before the demo. Since the software communication side is already working, the main risk is whether the physical sensor and actuator tests are fully ready and repeatable in time.
