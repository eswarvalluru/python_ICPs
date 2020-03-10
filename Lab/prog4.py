import requests
from bs4 import BeautifulSoup
html=requests.get("https://catalog.umkc.edu/course-offerings/graduate/comp-sci/")
bsoup = BeautifulSoup(html.content, "html.parser")
for i in bsoup.find_all('div',{'class':'courseblock'}):
    print(i.find('span',{'class':'code'}).text,'\t',i.find('p',{'class':'courseblockdesc'}).text,'\n')
    # print(i.find('p',{'class':'courseblockdesc'}).text,'\n')
