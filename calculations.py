import json
import sqlite3
import os
import requests
import math

#This file joins table NBA_Stats and NBA_Season to calculate what percentage of a team's points that a player had
#The calculations are written to a file called calculations.txt

def table_join():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.Player, NBA_Stats.PPG, NBA_Season.Home_Score, NBA_Season.Home FROM NBA_Season JOIN NBA_Stats ON NBA_Season.Home=NBA_Stats.Team LIMIT 25")
    x= cur.fetchall()
    y= list(x)
    final_lst= []
    fileobj=open('Calculations.txt','w')
    for i in y:
        calculated_num= i[1]
        calculated_num1= i[2]
        calculated_num2= calculated_num/calculated_num1
        final_var= calculated_num2 * 100
        final_var1= math.floor(final_var)
        final_lst.append("Player's Percentage Points of their Team: " + str(i[0]) + " " + str(final_var1) + '%')
        fileobj.write("Player's Percentage Points of their Team: " + str(i[0]) + " " + str(final_var1) + '%')
        fileobj.write('\n')
    return y
    fileobj.close()
table_join()
    