import os
import requests
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
PLACEHOLDER_IMAGE = "https://placehold.co/150"

def get_product_image(query: str = "product") -> str:
    """ Retorna uma imagem do Unsplash ou uma imagem placeholder. """
    if not UNSPLASH_ACCESS_KEY:
        return PLACEHOLDER_IMAGE  # Caso não tenha API Key, usa a placeholder

    url = f"https://api.unsplash.com/photos/random?query={query}&w=150&h=150&client_id={UNSPLASH_ACCESS_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        return data.get("urls", {}).get("small", PLACEHOLDER_IMAGE)
    except:
        return PLACEHOLDER_IMAGE
