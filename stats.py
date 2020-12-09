import json
import sqlite3
import os
import requests

def stats(year):
    player_names_1=[]
    player_stats=[]
    player_id=0
    url='https://api.sportradar.us/nba/trial/v7/en/seasons/{}/REG/leaders.json?api_key=jnxztd6mxbwm79hjxt6bm93q'.format(str(year))
    data=requests.get(url).text
    new_data=json.loads(data)
    y=new_data.get('categories')
    for val in range(44):
        data=y[val]['ranks']
        for x in data:
            player_name=x['player']['full_name']
            if player_name not in player_names_1:
                player_names_1.append(player_name)
                team=x['teams']
                for t in team:
                    team_name=t['name']
                avg_pts=x['average']['points']
                player_id+=1
                stat=(player_id,player_name,team_name,avg_pts) 
                player_stats.append(stat)    
    return player_stats      

def table():
    conn= sqlite3.connect('/Users/saracohen/Downloads/KateDannyBradleyFinalProject/Final.db')
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS NBA_Stats (Player_ID INTEGER, Player TEXT, Team TEXT, PPG INTEGER)")
    ppg=stats(2018)
    count=0
    cur.execute("SELECT Player_ID FROM NBA_Stats")
    player_id=cur.fetchall()
    for x in ppg:
        if count<=175:
            if x[0] not in player_id:
                cur.execute("INSERT INTO NBA_Stats (Player_ID, Player, Team, PPG) VALUES (?, ?, ?, ?)",(x[0], x[1], x[2], x[3]))
                count+=1
            else:
                continue
    conn.commit()
table()


#MAKE GLOBAL DATABASE

        
        
 