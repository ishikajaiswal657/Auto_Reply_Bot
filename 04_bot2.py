import pyautogui
import pyperclip
import time
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_last_message_from_sender(chat_log, sender_name="Len"):
    messages = chat_log.strip().split("/2025]")[-1]
    return sender_name in messages

def respond_to_chat():
    # Click icon to open chat app
    pyautogui.click(x=2105, y=1570)
    time.sleep(2)

    while True:
        # Drag to select chat history
        pyautogui.moveTo(1062, 383)
        pyautogui.dragTo(2755, 1381, duration=1.5, button='left')

        # Copy and paste text
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(1091, 768)
        time.sleep(2)
        chat_history = pyperclip.paste()

        if is_last_message_from_sender(chat_history):
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a student named Ishika who speaks Hindi and English. Respond like a casual Indian student."},
                    {"role": "user", "content": chat_history}
                ]
            )
            response = completion.choices[0].message.content
            pyperclip.copy(response)
            pyautogui.click(x=1376, y=1458)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(2)
            pyautogui.press('enter')

        time.sleep(5)  # wait before repeating

respond_to_chat()
