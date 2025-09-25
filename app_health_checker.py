#!/usr/bin/env python3
import requests
import logging

# Configure logging
logging.basicConfig(filename="app_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

URL = "https://shoaibcloud.bio"   # Replace with your app URL

def check_app_health():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP - Status {response.status_code}")
            logging.info(f"Application is UP - Status {response.status_code}")
        else:
            print(f"Application is DOWN - Status {response.status_code}")
            logging.warning(f"Application is DOWN - Status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN - Error: {e}")
        logging.error(f"Application is DOWN - Error: {e}")

if __name__ == "__main__":
    check_app_health()
