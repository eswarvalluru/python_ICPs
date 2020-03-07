import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Google'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
for t in text:
	if t.parent.name :
		output += '{} '.format(t)

print(output)