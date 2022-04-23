from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

url = "https://veiculos.fipe.org.br"

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup)