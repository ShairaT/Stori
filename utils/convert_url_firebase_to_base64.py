import requests
import requests
import base64

def convert_url_firebase_to_base64(url):
    response = requests.get(url)
    image_content = response.content
    return base64.b64encode(image_content).decode('utf-8')