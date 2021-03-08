import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os

def config():
    print("Call Config")
    return subscription_key, face_api_url

image_path = os.path.join(r'<path to your file>')
image_data = open(image_path, "rb")

subscription_key = "604bb28ffeaa484bb9054cc5ef42d86c"
face_api_url = 'https://azcogsvc.cognitiveservices.azure.com/face/v1.0/detect'

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()
print(faces)