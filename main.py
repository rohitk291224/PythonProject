# Python/PythonProject/main.py
import requests

def fetch_categories(api_url):
    try:
        response = requests.get(f"{api_url}/categories")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the API returns a JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching categories: {e}")
        return []

API_URL = "http://example.com/api"  # Replace with the actual API URL
categories = fetch_categories(API_URL)
print("Fetched categories:", categories)