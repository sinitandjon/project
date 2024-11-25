import requests

# Base API endpoint
BASE_URL = "https://api-lannuaire.service-public.fr/api/explore/v2.1/catalog/datasets/api-lannuaire-administration/records"
url="https://www.public.fr/"

# Example parameters for the API request
PARAMS = {
    "select": "nom,adresse,pivot",  # Fields to include in the results
    "limit": 10,                   # Number of records to retrieve
}

def fetch_articles(base_url, params):
    """
    Fetch articles or records from the Service Public API.
    
    Args:
        base_url (str): The base URL of the API.
        params (dict): Parameters for the API request.
        
    Returns:
        list: A list of articles or records.
    """
    try:
        # Send GET request to the API
        response = requests.get(base_url)#params=params)
        for el in response :
            print(el)
        print(response)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse JSON response
        data = response.json()
        if "records" in data:
            return data["records"]
        else:
            print("No records found in the response.")
            print(data)
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Fetch articles
articles = fetch_articles(url , PARAMS)

# Display the fetched articles
for article in articles:
    print(f"Name: {article.get('record', {}).get('fields', {}).get('nom', 'N/A')}")
    print(f"Address: {article.get('record', {}).get('fields', {}).get('adresse', 'N/A')}")
    print(f"Pivot: {article.get('record', {}).get('fields', {}).get('pivot', 'N/A')}")
    print("-" * 40)
