Apache Web Server Postmortem
Server Down

Incident Overview
The Apache Web Server experienced an unexpected service interruption on Port 80, leading to a brief outage. This postmortem provides a detailed account of the incident, its impact, root cause, resolution, and corrective measures taken.

Incident Timeline
Duration: Approximately the time it takes to brew a cup of coffee
Start Time: Just as your coffee was ready
End Time: Before you could take the first sip
How It All Began

Issue Detected: An abrupt alert on the monitoring dashboard
Actions Taken: Immediate investigation to identify the root cause
Misleading Investigation: Initial suspicion of a DDoS attack was discarded as the cause
Escalation: Involvement of infrastructure and network teams to address the issue
Incident Details
The Culprit Revealed

Root Cause: Port 80 was seized by an unauthorized service installation, causing a conflict with Apache's normal operations.
Resolution: The rogue installation was removed, Apache's configuration was adjusted, and the web server was brought back online.
Corrective and Preventative Measures
Lessons Learned and Actions Taken

Improved Monitoring: Implemented more robust monitoring systems to detect anomalies early.
Configuration Review: Conducted a thorough review of server configurations to prevent conflicts.
Enhanced Documentation: Updated documentation to avoid future port conflicts and aid in faster issue resolution.
Port Security: Implemented measures to ensure only authorized services can utilize critical ports.
Conclusion
By addressing the root cause of this incident and implementing corrective measures, we have taken steps to prevent future disruptions. Our goal is to maintain a stable and secure web service for all users.

For more technical details, refer to the full postmortem report.

This README provides a brief overview of the incident and steps taken for resolution. Please refer to the complete postmortem report for a more comprehensive understanding.





