import json
import sqlite3
import os
import requests
import time 

#Create Database 
conn = sqlite3.connect('/Users/bradleyharrison/Desktop/KateDannyBradleyFinalProject/Final.db')
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS Postseason")
cur.execute("CREATE TABLE IF NOT EXISTS Postseason (team TEXT, year INTEGER, postseason TEXT)")


#Retrieve which teams made the 2015-2016 NBA playoffs

def get_nba_api_data_2015_2016():
    lst_city=[]
    for l in range(1,90):
        url_2="https://www.balldontlie.io/api/v1/stats"
        try:
            ne=requests.get(url_2,
            params={'season':2015,
            'postseason':True,
            'start_date':'2016-04-15',
            'end_date':'2016-06-20',
            'page':l}).json()
            x=ne.get('data')
            for y in x:
                team=y['team']
                name=team['name']
                if name not in lst_city:
                    lst_city.append(name)
                    
                    
        except:
            None

    for name in lst_city:
        cur.execute("INSERT INTO Postseason (team, year, postseason) VALUES (?, ?, ?)",(name, 2015, 'yes'))


    return lst_city
get_nba_api_data_2015_2016()



#Retrieve which teams made the 2016-2017 NBA playoffs

def get_nba_api_data_2016_2017():       
    lst_city2=[]
    for l in range(1,82):
        url="https://www.balldontlie.io/api/v1/stats"
        try:
            ne=requests.get(url,
            params={'season':2016,
            'postseason':True,
            'start_date':'2017-04-13',
            'end_date':'2017-06-13',
            'page':l}).json()
            var=ne.get('data')
            for t in var:
                teams=t['team']
                name=teams['name']
                if name not in lst_city2:
                    lst_city2.append(name)
        except:
            None

    for name in lst_city2:
        cur.execute("INSERT INTO Postseason (team, year, postseason) VALUES (?, ?, ?)",(name, 2016, 'yes'))
    
    return lst_city2
get_nba_api_data_2016_2017()


#Retriev which teams made the 2017-2018 NBA playoffs

def get_nba_api_data_2017_2018():
    lst_city3=[]
    for l in range(1,90):
        url="https://www.balldontlie.io/api/v1/stats"
        try:
            ne=requests.get(url,
            params={'season':2017,
            'postseason':True,
            'start_date':'2018-04-13',
            'end_date':'2018-06-10',
            'page':l}).json()
            v=ne.get('data')
            for val in v:
                team_1=val['team']
                name=team_1['name']
                if name not in lst_city3:
                    lst_city3.append(name)
        except:
            None   

    for name in lst_city3:
        cur.execute("INSERT INTO Postseason (team, year, postseason) VALUES (?, ?, ?)",(name, 2017, 'yes'))
    

    return lst_city3
get_nba_api_data_2017_2018()
    
conn.commit()



def get_nba_data():
    nba_dict={}
    first=get_nba_api_data_2015_2016()
    second=get_nba_api_data_2016_2017()
    third=get_nba_api_data_2017_2018()
    nba_dict[2015]=first
    nba_dict[2016]=second
    nba_dict[2017]=third
    print(nba_dict)
#get_nba_data()





#list of each unique city
#final_city_list=['Did not make playoffs back to back',]
#for x in lst_city:
    #if x not in lst_city2:
        #final_city_list.append(x)
#for x in lst_city3:
    #if x not in lst_city2:
        #if x not in final_city_list:
            #final_city_list.append(x)
    #print(final_city_list)

    #list of each city 
#new_dict= {'total city playoffs':'count'}
#for x in lst_city:
    #new_dict[x]= new_dict.get(x,0) + 1
#for x in lst_city2:
    #new_dict[x]= new_dict.get(x,0) + 1
#for x in lst_city3:
    #new_dict[x]= new_dict.get(x,0) + 1
    #print(new_dict)

    




    

 

#setUpNBATable()

