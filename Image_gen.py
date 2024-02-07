import openai
from dotenv import load_dotenv
import os



load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def openai_image(user_prompt):
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=user_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error generating image."

print(openai_image("software bug Warrior"))