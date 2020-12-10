import requests 
import sqlite3
import json
import os


path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, 'final.db')
conn= sqlite3.connect(db)
cur = conn.cursor()

#cur.execute("DROP TABLE IF EXISTS Attendance")
#cur.execute("CREATE TABLE IF NOT EXISTS Attendance (rank INTEGER, team TEXT, homeav INTEGER, year INTEGER)")

from bs4 import BeautifulSoup
def nba_fan_attendance():
    id=0
    years=[2015,2016,2017,2018]
    teamsdata={}
    teamsdata2=[]
    for year in years:
        url='http://www.espn.com/nba/attendance/_/year/' + str(year)
        page=requests.get(url)
        if page.ok:
            soup=BeautifulSoup(page.content, 'html.parser')

            table=soup.find('table', class_= 'tablehead')
            rows=table.findAll('tr')
            

            for row in rows[2:]:
                vals=row.findAll('td')
                finalrank=vals[0].text.strip()
                homeaverage=vals[4].text.strip()
                #print(homeaverage)
                #roadaverage=vals[7].text.strip()
                #totalaverage=vals[10].text.strip()

                team1=row.findAll('td')
                for x in team1:
                    team=x.find('a')
                    if team!=None:
                        #print(team.text)
                        finalteam=team.text.strip()
                        teamsdata[finalteam]=id,homeaverage,finalrank
                        teamsdata2.append((id,finalteam,homeaverage,finalrank,year))
                        id+=1
    #print(teamsdata2)
    return teamsdata2
    #this is all to get it to limit how much data is added at once
#nba_fan_attendance()
def table():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS Attendance (id INTEGER, rank INTEGER, team TEXT, homeav INTEGER, year INTEGER)")
    data=nba_fan_attendance()
    count=0
    cur.execute("SELECT id FROM Attendance")
    game_ids=cur.fetchall()
    new_id = [i[j] for i in game_ids for j in range(len(i))]

    for x in data:
        if count<=25:
            if x[0] not in new_id:
                cur.execute("INSERT INTO Attendance (id,rank,team,homeav,year) VALUES (?,?,?,?,?)",(x[0],x[3],x[1],x[2],x[4]))
                count+=1
            else:
                continue

    conn.commit()
table()
    