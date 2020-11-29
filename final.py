#does this work
#question we are answering: How does an NBA team’s performance affect local businesses?
#first function will access the API's/website

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
    
    
get_nba_api_data()    
    




#second function will access and store at least 100 items in your database from each API/website in at least one table per API/website. 
# For at least one API you must have two tables that share a key
# You must not have duplicate data in your database!  Do not split data from one table into two! 
# Also, there should be only one database! 
#third function will limit how much data you store from an API into the database each time you execute your code to 25 or fewer items 
# The data must be stored in a SQLite database. This meansthat you must run the code that stores the data multiple times 
# to gather at least 100 items total without duplicating existing data or changing it.
#then we process the data- 3 functions
#first function is selecting some data from all of the tables in your database and calculate something from that data
#example for first function: Calculating # of hm items occur on a particular day of the week
#  or the average of the number of items per day.  
#second function: You must do at least one database jointo select your data
#third function: Write out the calculated data to a file as text
#Next step: at least 3 visualizations, different from what we did in lecture, maybe 2 more visualizations for extra credit