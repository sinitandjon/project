import requests

url = "http://127.0.0.1:8000/search/"
data = {"query": "olivier giroud"}

response = requests.get(url, json=data)

if response.status_code == 200:
    print("Embedding:", response.json())
else:
    print("Error:", response.status_code, response.text)
