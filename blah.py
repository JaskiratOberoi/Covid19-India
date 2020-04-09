import requests
import json
import pprint

data = requests.get('https://api.covid19india.org/data.json')
data = data.json()
TotalConfirmed = data["statewise"][0]["confirmed"]

pprint.pprint(TotalConfirmed)