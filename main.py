import requests
import pprint

parameters = {
    "q" : "html"
}

responce = requests.get("https://api.github.com/search/repositories", params = parameters)

print(responce.status_code)

responce_json = responce.json()
pprint.pprint(responce_json)