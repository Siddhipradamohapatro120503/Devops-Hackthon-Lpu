import Image_gen
import requests
from PIL import Image
from io import BytesIO

def url_to_png(image_url, output_path):
    try:
        response = requests.get(image_url)
        
        if response.status_code == 200:
           
            image = Image.open(BytesIO(response.content))
           
            image.save(output_path, format='PNG')
            print("Image saved as", output_path)
        else:
            print("Failed to download image. Status code:", response.status_code)
    except Exception as e:
        print("Error:", e)

# Example usage
image_url = Image_gen.openai_image("car in a vally")  # Replace with the actual image URL
output_path = "output.png"  # Output file path for the PNG image
url_to_png(image_url, output_path)
