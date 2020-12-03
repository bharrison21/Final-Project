import requests 
from bs4 import BeautifulSoup
def nba_fan_attendance(year):
    url='http://www.espn.com/nba/attendance/_/year/' + str(year)
    page=requests.get(url)
    if page.ok:
        soup=BeautifulSoup(page.content, 'html.parser')

        table=soup.find('table')
        rows=table.findAll('tr')

        teamsdata={}

        for row in rows[2:]:

            vals=row.findAll('td')
            finalrank=vals[0].text.strip()
            homeaverage=vals[4].text.strip()
            #roadaverage=vals[7].text.strip()
            #totalaverage=vals[10].text.strip()

            team1=row.findAll('td')
            for x in team1:
                team=x.find('a')
                if team!=None:
                    #print(team.text)
                    finalteam=team.text.strip()
                    teamsdata[finalteam]=[homeaverage,finalrank]
        print(teamsdata)
nba_fan_attendance(2017)


    