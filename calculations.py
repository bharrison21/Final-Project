import json
import sqlite3
import os
import requests
import math
def table_join():
    conn= sqlite3.connect('/Users/saracohen/Downloads/KateDannyBradleyFinalProject/Final.db')
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.Player, NBA_Stats.PPG, NBA_Season.Home_Score, NBA_Season.Home FROM NBA_Season JOIN NBA_Stats ON NBA_Season.Home=NBA_Stats.Team LIMIT 25")
    x= cur.fetchall()
    y= list(x)
    final_lst= []
    for i in y:
        calculated_num= i[1]
        calculated_num1= i[2]
        calculated_num2= calculated_num/calculated_num1
        final_var= calculated_num2 * 100
        final_var1= math.floor(final_var)
        final_lst.append("Player's Percentage Points of their Team: " + str(i[0]) + " " + str(final_var1) + '%')
    return y
table_join()
    
    