# Hunt 02 — Unusual PowerShell Process

## Question
Are PowerShell processes being launched with unusual command-line arguments or unexpected parent processes?

## Hypothesis
Encoded command indicators, unusual parent-child relationships, or execution from unexpected paths may deserve review. These signals can also occur in legitimate administration.

## Data required
Sysmon Event ID 1 or another process-creation source with image, command line, parent image, user, and timestamp.

## Procedure
1. Confirm Sysmon process-creation telemetry is being collected.
2. Search a defined time window for powershell.exe and pwsh.exe.
3. Review command line, parent process, user, host, and execution time.
4. Compare the activity with known administrative tools and scheduled tasks.
5. Pivot to related network, file, and script-block telemetry only if available.
6. Record benign explanation, suspicious evidence, or unresolved gaps.

## Safe validation
On your own Windows lab endpoint, open PowerShell normally and run a harmless command such as Get-Date. Confirm process telemetry appears. Do not execute downloaded payloads or obfuscated scripts for this exercise.

## Outcome
Not tested. Add the event and screenshot after practical validation.
