import openai
from dotenv import load_dotenv
import os

load_dotenv()
# client = OpenAI()
openai.api_key = os.getenv('OPENAI_API_KEY')


response = openai.Image.create(
  prompt="Photo of Pinocchio riding a bike on Central Park",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
image_url #the URL of the generated image