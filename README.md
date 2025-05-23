**Moodle to Google**


This Python script copies events from a Moodle calendar (often used by schools and universities) to Google Calendar after filtering unwanted events.

While you can simply point Google Calendar to a calendar at another url, I found that my Moodle calendar for university had too many unnecessary events present that I wanted to remove. They were not repeating events so I would have to go through an entire year and delete them 1 by 1. This script does that for you using the Google Calendar API.

![image](https://github.com/user-attachments/assets/ac3567dc-8c53-482b-8b77-c3f3c6a851f7)

**What does the script do?**
- Open a terminal for user input
- Ask for a Google account
- Ask for a url for a Moodle calendar
- Ask for tags that you do not want to appear in the final events
- Filter the events from the Moodle calendar with the tags
- Ask for a Google Calendar calendar ID
- Add the final events to the correct calendar on Google Calendar
- Information is stored locally too so that the next execution of the script is optionally less tedious. This info includes a token for Google account sign in, the Moodle calendar URL and the Google Calendar calendar ID.

![image](https://github.com/user-attachments/assets/25943081-8b14-4bc6-a892-a57bb5cdbbb4)

**Requirements:**
- Python 3.11.9
- API key (given by me)
- Necessary python libraries are automatically installed when the script runs.

**Setup guide:**
[Setup guide.pdf](https://github.com/user-attachments/files/20049338/Setup.guide.pdf)
