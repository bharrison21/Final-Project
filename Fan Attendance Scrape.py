import requests 
import sqlite3
import json
import os


conn=sqlite3.connect('/Users/kategould/Documents/KateDannyBradleyFinalProject/Final.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Attendance")
cur.execute("CREATE TABLE IF NOT EXISTS Attendance (rank INTEGER, team TEXT, homeav INTEGER, year INTEGER)")

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
    for team in teamsdata:
        rank=teamsdata[team][1]
        homeaverage=teamsdata[team][0]
        cur.execute("INSERT INTO Attendance (rank,team,homeav,year) VALUES (?,?,?,?)",(rank,team,homeaverage,year))
        #print(teamsdata)
    conn.commit()
nba_fan_attendance(2017)
nba_fan_attendance(2018)
#SELECT Attendance.homeav,Attendance.team FROM Postseason JOIN attendance ON Postseason.team=Attendance.team WHERE Attendance.year=2017 AND postseason.postseason="yes" ORDER BY Attendance.rank

    