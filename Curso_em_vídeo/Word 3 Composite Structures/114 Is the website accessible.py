import urllib
import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("Deu erro")
else:
    print("Tudo ok")