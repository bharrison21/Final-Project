import json
import sqlite3
import os
import requests


def get_nba_api_data():

    #Retrieve which teams made the 2015-2016 NBA playoffs
    lst_city=[]
    for l in range(1,22):
        url_2="https://www.balldontlie.io/api/v1/stats"
        ne=requests.get(url_2,
        params={'season':2015,
        'postseason':True,
        'start_date':'2016-04-15',
        'end_date':'2016-06-20',
        'page':l})
        more_data=json.loads(ne.text)
        x=more_data.get('data')
        for y in x:
            team=y['team']
            city=team['city']
            if city not in lst_city:
                lst_city.append(city)
    statement='2015-2016 Playoffs: ' + str(lst_city)
    print('\n')
    print(statement)


    #Retrieve which teams made the 2016-2017 NBA playoffs
    lst_city2=[]
    for l in range(1,15):
        url="https://www.balldontlie.io/api/v1/stats"
        ne=requests.get(url,
        params={'season':2016,
        'postseason':True,
        'start_date':'2017-04-13',
        'end_date':'2017-06-13',
        'page':l})
        data=json.loads(ne.text)
        var=data.get('data')
        for t in var:
            teams=t['team']
            cities=teams['city']
            if cities not in lst_city2:
                lst_city2.append(cities)
    statement2='2016-2017 Playoffs: ' + str(lst_city2)
    print(statement2)

    #Retriev which teams made the 2017-2018 NBA playoffs
    lst_city3=[]
    for l in range(1,15):
        url="https://www.balldontlie.io/api/v1/stats"
        ne=requests.get(url,
        params={'season':2017,
        'postseason':True,
        'start_date':'2018-04-13',
        'end_date':'2018-06-10',
        'page':l})
        fin_data=json.loads(ne.text)
        v=fin_data.get('data')
        for val in v:
            team_1=val['team']
            city_1=team_1['city']
            if city_1 not in lst_city3:
                lst_city3.append(city_1)
    statement3='2017-2018 Playoffs: ' + str(lst_city3)
    print(statement3)
    final_city_list= []
    for x in lst_city:
        if x not in lst_city2:
            final_city_list.append(x)
    for x in lst_city3:
        if x not in lst_city2:
            if x not in final_city_list:
                final_city_list.append(x)
    print(final_city_list)
    new_dict= {}
    for x in lst_city:
        new_dict[x]= new_dict.get(x,0) + 1
    for x in lst_city2:
        new_dict[x]= new_dict.get(x,0) + 1
    for x in lst_city3:
        new_dict[x]= new_dict.get(x,0) + 1
    print(new_dict)
    print(len(new_dict))
get_nba_api_data()
    


 
    return [statement,statement2,statement3]



def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def setUpNBATable(data):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+'nba.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Postseason")
    cur.execute("CREATE TABLE Postseason (team TEXT PRIMARY KEY, season TEXT)")
    for i in range(len(lst_city)):
        teamname=get_nba_api_data[i]
        season=get_nba_api_data[:3]
        cur.execute("INSERT INTO Postseason (team,season) VALUES (?,?)",(teamname,season))
    

#get_nba_api_data() 

setUpNBATable(get_nba_api_data())

