import requests
import os
from dotenv import load_dotenv
load_dotenv()

def make_gapi_request():
    api_key = os.getenv("api_key1")
    symbol = "XAU"
    curr = "USD"
    date = "/20240313"

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.text
        print(result)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

make_gapi_request()