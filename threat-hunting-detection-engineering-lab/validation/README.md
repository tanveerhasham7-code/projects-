# Validation Lab

Every detection must have a written test plan before it is considered validated.

For each test record:
- Detection ID and rule version
- Date/time and time zone
- Endpoint and telemetry source
- Preconditions and audit configuration
- Exact benign test action
- Expected event and fields
- Actual event and alert
- Result: Pass / Fail / Inconclusive / Not run
- False-positive observations
- Screenshot filename
- Analyst notes and limitations

Never claim a test passed because the rule merely loaded. A pass requires the expected behavior to generate the expected telemetry and detection outcome.
