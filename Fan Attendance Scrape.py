import requests 
from bs4 import BeautifulSoup

url='http://www.apbr.org/attendance.html'
page=requests.get(url)
if page.ok:
    soup=BeautifulSoup(page.content, 'html.parser')
    team=soup.find('pre')
    print(team)
    

    