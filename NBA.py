import json
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
    
    print(statement)
    print('\n')

    #Retrieve which teams made the 2016-2017 NBA playoffs
    lst_city2=[]
    for l in range(1,5):
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
    print('\n')

    #Retriev which teams made the 2017-2018 NBA playoffs
    lst_city3=[]
    for l in range(1,5):
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


get_nba_api_data()    
    


