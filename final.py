#does this work
#question we are answering: How does an NBA team’s performance affect local businesses?
#first function will access the API's/website

import json
import os
import requests


kate_stockapikey='UQPW0KR0NTZ7ZUUO'


#nba_stats_url='http://stats.nba.com/stats/teamdashboardbyyearoveryear/?measureType=Base&perMode=PerGame&plusMinus=N&paceAdjust=N&rank=N&leagueId=00&season=2020-21&seasonType=Regular+Season&poRound=0&teamId=1610612745&outcome=&location=&month=0&seasonSegment=&dateFrom=&dateTo=&opponentTeamId=0&vsConference=&vsDivision=&gameSegment=&period=0&shotClockRange=&lastNGames=0'
#r=requests.get(nba_stats_url)
#nbadata=json.loads(r.text)
def get_nba_api_data():

    #Retrieve seasons we want
    url_1='https://www.balldontlie.io/api/v1/games'
    re=requests.get(url_1, 
    params={'seasons':[2015,2016,2017,2018,2019],
    'per_page':100})
    all_data=json.loads(re.text)
    

    #Retreive Stats from players
    url_2='https://www.balldontlie.io/api/v1/stats'
    ne=requests.get(url_2,
    params={'seasons':[2015,2016,2017,2018,2019],
    'per_page':100})
    more_data=json.loads(ne.text)
    x=more_data.get('data')
    lst_id=[]
    for y in x:
        player=y['player']
        lst_id.append(player['id'])

        



    #Retrieve Players from those years
    url = "https://www.balldontlie.io/api/v1/players"
    re=requests.get(url,
    params={"per_page":100})
    
    data=json.loads(re.text)
    first_dict=data.get('data')
    lst_names=[]
    for x in first_dict:
        first=(x['first_name'])
        last=(x['last_name'])
        name=(first+' '+last)
        if x['id'] in lst_id:
            lst_names.append(name)
    print(lst_names)
    
    

get_nba_api_data()
def get_stock_api_data(kate_stockapikey):
    stock_url='https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey='+kate_stockapikey
    re=requests.get(stock_url)
    data=json.loads(re.text)
    print(data)

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