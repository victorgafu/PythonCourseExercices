import requests

url = "http://www.google.com"
response = requests.get(url)
print(f"Your request to {url} came back as status code: {response.status_code}")
