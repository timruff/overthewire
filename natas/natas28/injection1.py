import requests
import binascii
import urllib
import base64
from colorama import Fore, Style

url = "http://natas28.natas.labs.overthewire.org/index.php"
s = requests.Session()
s.auth = ('natas28', 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')

sample = ""

while len(sample) < 16:
    data = {'query':sample}
    r = s.post(url, data=data)
    cipher = r.url.split('=')[1]
    cipher = urllib.parse.unquote(cipher)
    print("[*] %d chars.\t| %s" % (len(sample), cipher))
    sample += 'a'




