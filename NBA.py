import json
import sqlite3
import os
import requests
import time 

<<<<<<< HEAD
#Create function to get dictionary of NBA Teams and their respecitve ID's from the API 
def get_nba_teams_id():
    team={}
    for l in range(1,1315):
        if len(team)==30:
            break
=======
#Create Database 
#conn = sqlite3.connect('/Users/bradleyharrison/Desktop/KateDannyBradleyFinalProject/Final.db')
conn=sqlite3.connect('/Users/kategould/Documents/KateDannyBradleyFinalProject/Final.db')
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS Postseason")
cur.execute("CREATE TABLE IF NOT EXISTS Postseason (team TEXT, year INTEGER, postseason TEXT)")


#Retrieve which teams made the 2015-2016 NBA playoffs

def get_nba_api_data_2015_2016():
    lst_city=[]
    for l in range(1,90):
>>>>>>> c041b6bb30ff8276425f2f2696dc10914a6d3977
        url_2="https://www.balldontlie.io/api/v1/stats"
        try:
            ne=requests.get(url_2,
            params={
            'start_date':'2018-10-15',
            'end_date':'2019-06-11',
            'page':l}).json()
            x=ne.get('data')
            for y in x:
                team_id=y['game']['home_team_id']
                players_team_id=y['team']['id']
                team_name=y['team']['name']
                if team_id==players_team_id:
                    if team_id not in team.keys():
                        team[team_id]=team_name
        except:
            None
    return team

#Create function to pull every NBA game from the 2018-2019 season 
#with the date, home team, home team score, away team, away team score, and winner 
def get_nba_api_data():
    team_and_id=get_nba_teams_id()
    conn = sqlite3.connect('/Users/bradleyharrison/Desktop/KateDannyBradleyFinalProject/Final.db')
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS NBA_Season (Date TEXT, Home TEXT, Home_Score INTEGER, Away TEXT, Away_Score INTEGER, Winner TEXT)")
    for l in range(1,1315):
        url_2="https://www.balldontlie.io/api/v1/stats"
        try:
            ne=requests.get(url_2,
            params={
            'start_date':'2018-10-15',
            'end_date':'2019-06-11',
            'page':l}).json()
            x=ne.get('data')  
            first=x[0]

            date=first['game']['date']
            date=date.split('T')
            date=date[0]
            #date is a str
            
            
            home_team_id=first['game']['home_team_id']
            home_team=team_and_id[home_team_id]
            home_team_score=first['game']['home_team_score']


            away_team_id=first['game']['visitor_team_id']
            away_team=team_and_id[away_team_id]
            away_team_score=first['game']['visitor_team_score']

            winner=''
            if home_team_score>away_team_score:
                winner=home_team
            else:
                winner=away_team

            cur.execute("INSERT INTO NBA_Season (Date, Home, Home_Score, Away, Away_Score, Winner) VALUES (?, ?, ?, ?, ?, ?)",(date, home_team, home_team_score, away_team, away_team_score, winner))
            
            print(date,home_team,home_team_score,away_team,away_team_score,winner)       
        except:
            None   
        

    conn.commit() 
get_nba_api_data()

#create database and limit to 25 
def table_setup():
    conn = sqlite3.connect('/Users/bradleyharrison/Desktop/KateDannyBradleyFinalProject/Final.db')
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS NBA_Season (Date TEXT, Home TEXT, Home_Score INTEGER, Away TEXT, Away_Score INTEGER, Winner TEXT)")
    data_1=get_nba_api_data()
    #count=0
    #for x in data_1:
        #print(x[0])
        # if count==24:
        #     break
        # if cur.execute("SELECT Date FROM NBA_Season WHERE Date IS NULL"):
        #     cur.execute("INSERT INTO NBA_Season (Date, Home, Home_Score, Away, Away_Score, Winner) VALUES (?, ?, ?, ?, ?, ?)",(x[0], x[1], x[2], x[3], x[4], x[5]))
        #     count+=1
    conn.commit()
#table_setup()
