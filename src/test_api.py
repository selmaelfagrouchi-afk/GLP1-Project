import requests

url = "https://api.fda.gov/drug/event.json"

params = {
    "search": 'patient.drug.openfda.generic_name:"semaglutide"',
    "count": "patient.reaction.reactionmeddrapt.exact",
    "limit": 10,
}

reponse = requests.get(url, params=params)
print("Code de réponse :", reponse.status_code)

donnees = reponse.json()
for ligne in donnees["results"]:
    print(ligne["term"], ligne["count"])
