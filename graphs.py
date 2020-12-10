import matplotlib
import matplotlib.pyplot as plt 
import sqlite3
import numpy as np
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
    return plt.show()
make_raptors_plot()
def nba_team_ppg():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.Player FROM NBA_Stats WHERE Team = 'Raptors'")
    x= cur.fetchall()
