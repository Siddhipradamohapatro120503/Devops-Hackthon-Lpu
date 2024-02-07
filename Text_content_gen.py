from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')



def openai_generate(user_prompt):
    try:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
         messages=[
            {"role": "system", "content": "You are a expert Linkedin Content Creator."},
            {"role": "user", "content": user_prompt},
            ],         
    )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error generating linkedin content."


print(openai_generate("I am a software developer."))