import requests
from bs4 import beautifulsoup4
import os
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(html.content, "html.parser")
print(bsObj.h1)
print(soup.title.string)