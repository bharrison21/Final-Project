import json
import sqlite3
import os
import requests

conn = sqlite3.connect('/Users/bradleyharrison/Desktop/KateDannyBradleyFinalProject/Final.db')
cur = conn.cursor() 
cur.execute("CREATE TABLE IF NOT EXISTS NBA_Stats (Player TEXT, Team TEXT, PPG INTEGER)")
url='https://api.sportradar.us/nba/trial/v7/en/seasons/2018/REG/leaders.json?api_key=jnxztd6mxbwm79hjxt6bm93q'
data=requests.get(url).text
new_data=json.loads(data)
y=new_data.get('categories')
for val in range(44):
    data=y[val]['ranks']
    for x in data:
        player_name=x['player']['full_name']
        team=x['teams']
        for t in team:
            team_name=t['name']
        avg_pts=x['average']['points']
        print("Player: " + player_name + ",","Team: " + team_name + ",","PPG: " + str(avg_pts))
        cur.execute("INSERT INTO NBA_Stats (Player, Team, PPG) VALUES (?, ?, ?)",(player_name, team, avg_pts,))
conn.commit()



