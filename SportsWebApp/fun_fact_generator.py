import json

import requests


def generate_fun_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = json.loads(response.text)  # fetch json data
    useless_fact = data["text"]
    return useless_fact
