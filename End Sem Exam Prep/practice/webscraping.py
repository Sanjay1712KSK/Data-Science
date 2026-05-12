import requests as r
from bs4 import BeautifulSoup as bs
url="https://www.scrapethissite.com/pages/"
res=r.get(url)
soup=bs(res.text,"html.parser")
if soup.title:
    print(soup.title.text)
else:
    print("No title found")