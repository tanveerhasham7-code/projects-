# 12 — Purple-Team Capstone

## Scenario
You are a junior security analyst supporting a small organization. Your task is to assess a controlled three-machine lab, simulate a few harmless behaviors, and explain how well the defensive monitoring detects them.

## Required tasks
1. Complete the asset inventory for Kali, Windows, and Ubuntu.
2. Document the isolated network design.
3. Verify Windows and Ubuntu agent health.
4. Confirm at least one useful Windows event is visible locally and in Wazuh.
5. Confirm at least one Ubuntu authentication or web event is visible locally and in Wazuh.
6. Run the limited Nmap service inventory against the Ubuntu VM.
7. Run the three-attempt manual SSH failure exercise, if SSH and test account are configured.
8. Run the two harmless HTTP GET requests, if a lab web service is configured.
9. Write at least two detection specifications.
10. Validate at least one detection end to end.
11. Complete one investigation report.
12. Document telemetry gaps, false positives, and improvements.

## Final deliverables
- Architecture diagram and asset inventory.
- Baseline evidence.
- Kali activity log.
- Windows and Ubuntu event evidence.
- Wazuh alert evidence, or a clear explanation if no alert occurred.
- Detection specifications and test records.
- Investigation report.
- Final lessons-learned summary.

## Assessment rubric

| Area | Weight |
|---|---:|
| Safe isolation and scope | 15% |
| System inventory and baseline | 10% |
| Telemetry verification | 20% |
| Safe test execution and evidence | 15% |
| Detection logic and validation | 20% |
| Investigation quality and reporting | 20% |

A missing alert can still be a valuable result if you identify the telemetry or rule gap accurately. Never fabricate a pass.
