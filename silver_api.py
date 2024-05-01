import requests
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def make_gapi_request():
    api_key = os.getenv('api_key2')
    symbol = "XAG"
    curr = "USD"
    date = "/20240430"

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        
        with open('silver_data.csv',mode='w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(result.keys())
            writer.writerow(result.values())

        print("CSV file created.")


    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

make_gapi_request()