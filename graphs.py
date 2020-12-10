import matplotlib
import matplotlib.pyplot as plt 
import sqlite3
import numpy as np
import os
#data for plotting
def make_raptors_plot():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.Player FROM NBA_Stats WHERE Team = 'Raptors'")
    x= cur.fetchall()
    z= []
    a= []
    for i in x:
        i= str(i)
        a.append(i)
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE Team = 'Raptors'")
    y= cur.fetchall()
    lst= []
    for i in y:
        lst.append(i)
    for i in lst:
        i= ' '.join(map(str, y))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        q= i.split(' ')
    for i in q:
        i= float(i)
        z.append(i)
    fig, ax = plt.subplots() 
    plt.bar(a, z)
    ax.set_xlabel('Player', fontsize= 16, color= 'r')
    ax.set_ylabel('PPG', fontsize= 16, color= 'r')
    ax.set_title('Leading points scorers on 2018-2019 Raptors')
    plt.xticks(rotation= 45)
    plt.savefig("test.png",bbox_inches='tight')
    matplotlib.pyplot.subplots_adjust(left=None, bottom=0.37, right=None, top=None, wspace=None, hspace=None)
    plt.show()
    print(z)
    return z
make_raptors_plot()
def win_percentage():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Season.Home FROM NBA_Season")
    x= cur.fetchall()
    cur.execute("SELECT NBA_Season.Away FROM NBA_Season")
    y= cur.fetchall()
    cur.execute("SELECT NBA_Season.Winner FROM NBA_Season")
    z= cur.fetchall()
    d= {}
    for i in x:
        i= ' '.join(map(str, x))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
    for a in i.split(' '):
        if a not in d:
            d[a]= 1
        else:
            d[a]+=1
    for i in y:
        i= ' '.join(map(str, y))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
    for a in i.split(' '):
        if a not in d:
            d[a] = 1
        else:
            d[a]+=1
    d1= {}
    for i in z:
        i= ' '.join(map(str, z))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
    for a in i.split(' '):
        if a not in d1:
            d1[a] = 1
        else:
            d1[a] +=1

    total_games_played= []
    for x in d.items():
        total_games_played.append(x[1])
    total_games_won= []
    for x in d1.items():
        total_games_won.append(x[1])

    lst_1= []
    count= 0
    bradley= []
    for x in d.items():
        wp= (total_games_won[count]/total_games_played[count]) * 100
        bradley.append(wp)
        win_percentage= "The win percentage for the " + str(x[0]) + ' was ' + str((total_games_won[count]/total_games_played[count]) * 100) + '%'
        lst_1.append(win_percentage)
        count+=1
    team_lst= []
    for x in d.items():
        team_lst.append(x[0])

    fig, ax = plt.subplots() 
    plt.bar(team_lst, bradley)
    ax.set_xlabel('Team', fontsize= 16, color= 'b')
    ax.set_ylabel('Win Percentage', fontsize= 16, color= 'b')
    ax.set_title('Each Teams Win Percentage for the 2018-2019')
    plt.xticks(rotation= 90)
    plt.savefig("test.png",bbox_inches='tight')
    matplotlib.pyplot.subplots_adjust(left=None, bottom=0.3, right=None, top=None, wspace=None, hspace=None)
    plt.show()
    print(bradley)
    return bradley
win_percentage()

# path = os.path.dirname(os.path.abspath(__file__))
# db = os.path.join(path, 'final.db')
# conn= sqlite3.connect(db)
# cur = conn.cursor() 
# cur.execute("SELECT NBA_Season.Home FROM NBA_Season")
# x= cur.fetchall()
# cur.execute("SELECT NBA_Season.Away FROM NBA_Season")
# y= cur.fetchall()
# cur.execute("SELECT NBA_Season.Winner FROM NBA_Season")
# z= cur.fetchall()
