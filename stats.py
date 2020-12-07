import json
import sqlite3
import os
import requests

conn = sqlite3.connect('/Users/bradleyharrison/Desktop/KateDannyBradleyFinalProject/Final.db')
cur = conn.cursor() 
cur.execute("CREATE TABLE IF NOT EXISTS NBA_Stats (Player TEXT, Team TEXT, PPG INTEGER)")

def stats(year,limit):
    url='https://api.sportradar.us/nba/trial/v7/en/seasons/{}/REG/leaders.json?api_key=jnxztd6mxbwm79hjxt6bm93q'.format(str(year))
    data=requests.get(url).text
    new_data=json.loads(data)
    y=new_data.get('categories')
    for val in range(44):
        data=y[val]['ranks']

        cur.execute("SELECT * FROM NBA_Stats")
        newlen=cur.fetchall()
        while len(newlen)<=limit:
            for x in data:
                if len(newlen)>limit:
                    break
                exists=cur.execute("SELECT Player FROM NBA_Stats WHERE Player=?",(x['player']['full_name'], ))
                if cur.fetchone():
                    continue
                else:
                    player_name=x['player']['full_name']
                    team=x['teams']
                    for t in team:
                        team_name=t['name']
                    avg_pts=x['average']['points']
                    print("Player: " + player_name + ",","Team: " + team_name + ",","PPG: " + str(avg_pts))
                    cur.execute("INSERT INTO NBA_Stats (Player, Team, PPG) VALUES (?, ?, ?)",(str(player_name), str(team_name), int(avg_pts),))
                    cur.execute("SELECT * FROM NBA_Stats")
                    newlen=cur.fetchall()
    conn.commit()
stats(2018,30)



# cur.execute("SELECT * FROM Attendance")
#     newlen=cur.fetchall()
#     while len(newlen)<=limit:
#         for team in teamsdata:
#             if len(newlen)>limit:
#                 break
#             exists=cur.execute("SELECT team FROM Attendance WHERE team=?",(team, ))
#             if cur.fetchone():
#                 continue
#             else:
#                 rank=teamsdata[team][1]
#                 homeaverage=teamsdata[team][0]
#                 cur.execute("INSERT INTO Attendance (rank,team,homeav,year) VALUES (?,?,?,?)",(rank,team,homeaverage,year))
#                 cur.execute("SELECT * FROM Attendance")
#                 newlen=cur.fetchall()