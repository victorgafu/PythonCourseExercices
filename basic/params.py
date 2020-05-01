import requests

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat"}
)

data = response.json()
for result in data["results"]:
    print(result["joke"])
print(f"status: {data['status']}")
