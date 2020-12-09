import json
import sqlite3
import os
import requests

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+'Final.db')
#conn = sqlite3.connect('/Users/kategould/Documents/KateDannyBradleyFinalProject/Final.db')
cur = conn.cursor()
#cur.execute("DROP TABLE IF EXISTS NBA_Stats")
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
                    #print("Player: " + player_name + ",","Team: " + team_name + ",","PPG: " + str(avg_pts))
                    cur.execute("INSERT INTO NBA_Stats (Player, Team, PPG) VALUES (?, ?, ?)",(str(player_name), str(team_name), int(avg_pts),))
                    cur.execute("SELECT * FROM NBA_Stats")
                    newlen=cur.fetchall()
    conn.commit()
stats(2018,28)