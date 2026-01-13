AUTO_REPLY_CHAT_BOT🤖
An automated chat assistant built with Python that uses GUI automation to interact with 
messaging applications and OpenAI's GPT-3.5 to generate human-like responses.

The bot adopts the persona of Ishika, a casual Indian student who communicates
naturally using a blend of Hindi and English (Hinglish).

🚀 Features:
>Persona-Driven Responses: Responds as a casual Indian student named Ishika
>GUI Automation: Uses PyAutoGUI to physically interact with the chat application on your desktop
>Smart Message Detection: Monitors chat history and only responds when a specific sender sends the last message
>Context Aware: Analyzes the recent chat log to ensure the response fits the conversation history.

🛠️ Technical Stack:
Language: Python
Automation: PyAutoGUI (mouse/keyboard control)
Clipboard Management: Pyperclip
AI Engine: OpenAI API (GPT-3.5-Turbo)
Environment Management: python-dotenv (for secure API key storage)

📋 Prerequisites:
Before running the bot, ensure you have the required libraries installed:
Bashpip install pyautogui pyperclip openai python-dotenv

⚙️ Setup & Calibration:
Since this bot uses screen coordinates, you must calibrate it for your specific monitor resolution.

1. Get Coordinates:
Run 01_get_cursor.py and hover your mouse over the following areas to note their $(X, Y)$ positions:
.The chat app icon on your taskbar.
.The top-left and bottom-right of the chat history area.
.The message input box.
2.Update Scripts: Update the coordinates in 04_bot2.py (or your main script) using the values you found.
3.API Security:
.Create a .env file in the root directory.
.Add your OpenAI API key: OPENAI_API_KEY=your_key_here.

📂 Project Structure
.01_get_cursor.py: Utility script to find screen coordinates for calibration.
.02_openai.py: Core logic for interacting with the OpenAI API and setting the "Ishika" persona.
.04_bot2.py: The main automation loop that handles clicking, copying, and replying.

⚠️ Disclaimer
This project is for educational purposes. 
Automated interaction with some messaging platforms may violate their Terms of Service.
Use responsibly.
