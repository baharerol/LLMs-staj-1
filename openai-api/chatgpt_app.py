import openai
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_chat(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "Sen yardımcı bir yapay zeka asistanısın."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Hata oluştu: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Çıkılıyor...")
            break
        response = gpt_chat(user_input)
        print("ChatGPT:", response)