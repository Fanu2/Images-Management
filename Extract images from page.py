import os
import requests
from PIL import Image
from io import BytesIO

# Directory to save the images
save_directory = '/home/jasvir/Music/Movie work/Rosa/'
os.makedirs(save_directory, exist_ok=True)

# URL of the Hugging Face Space (You will need to specify the correct URL for image fetching)
base_url = 'https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory'

# Function to fetch and save images
def fetch_and_save_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check for HTTP errors
        image = Image.open(BytesIO(response.content))
        image.save(save_path, 'PNG')
        print(f"Image saved to {save_path}")
    except Exception as e:
        print(f"Error fetching or saving image: {e}")

# Example list of image URLs (You need to replace these with actual URLs)
image_urls = [
    f"{base_url}/image1.png",
    f"{base_url}/image2.png"
    # Add more URLs as needed
]

# Save images
for i, url in enumerate(image_urls):
    save_path = os.path.join(save_directory, f'image_{i + 1}.png')
    fetch_and_save_image(url, save_path)
