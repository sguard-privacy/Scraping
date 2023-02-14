from bs4 import BeautifulSoup
import requests

url = "https://sleyter.fr"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

