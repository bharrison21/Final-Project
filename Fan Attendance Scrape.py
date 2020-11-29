import requests 
from bs4 import BeautifulSoup
def nba_fan_attendance(year):
    url='http://www.espn.com/nba/attendance/_/year/' + str(year)
    page=requests.get(url)
    if page.ok:
        soup=BeautifulSoup(page.content, 'html.parser')
        team=soup.find('div', class_='span-6')
        team2= team.find('div', class_= 'mod-container mod-table mod-no-header mod-no-footer')
        team3= team2.find('div', class_= 'mod-content')
        team4= team3.find('table')
        team5= team4.find('tbody')
        print(team5)
nba_fan_attendance(2016)


    