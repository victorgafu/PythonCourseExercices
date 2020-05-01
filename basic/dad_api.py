import requests
import pyfiglet
from termcolor import colored
from random import choice

url = "https://icanhazdadjoke.com/search"


def get_data(topic):
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    )
    return response.json()


def display_joke(data):
    total_jokes = data["total_jokes"]
    results = data["results"]
    topic = data["search_term"]
    if total_jokes > 0:
        print(f"I've got {total_jokes} joke about {topic}. Here it is:")
        print(choice(results)["joke"])
    else:
        print(f"Sorry, I don't have any jokes about {topic}! Please try again")


header = pyfiglet.figlet_format("DAD JOKES!!!")
print(colored(header, color="blue"))

theme = input("Let me tell you a joke! Give me a topic: ")
display_joke(get_data(theme))
