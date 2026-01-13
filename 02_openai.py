import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
 api_key=os.getenv("OPENAI_API_KEY")
)
#https://platform.openai.com/account/api-keys.
def get_ishika_response(chat_log):
    """
    Analyzes chat history and returns a response in Ishika's persona.
    """
    completion = client.chat.completions.create(
         model = "gpt-3.5-turbo",
         messages=[
             {"role": "system", "content":"You are a person named Ishika who speaks Hindi and English. "
                           "She is a student from India. Analyze the chat history and respond naturally."},
             {"role":"user","content": chat_log} # type: ignore
        ]
    )
    print(completion.choices[0].message.content)