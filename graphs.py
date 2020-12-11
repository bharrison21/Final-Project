import matplotlib
import matplotlib.pyplot as plt 
import sqlite3
import numpy as np
import os
import random
# data for plotting



def make_raptors_plot():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.Player FROM NBA_Stats WHERE NBA_Stats.Team = 'Raptors'")
    x= cur.fetchall()
    players=[i[j] for i in x for j in range(len(i))]
    z= []
    a= []
    for i in x:
        i= str(i)
        a.append(i)
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE Team = 'Raptors'")
    y= cur.fetchall()
    debug = [i[j] for i in y for j in range(len(i))]
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
    return z
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
    new_dict= dict(zip(team_lst, bradley))
    return new_dict


def final_graph():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Kings'")
    sac_kings= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Raptors'")
    tor_raptors= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Bucks'")
    mil_bucks= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Clippers'")
    la_clippers= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Knicks'")
    ny_knicks= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Cavaliers'")
    cle_cavaliers= cur.fetchall()
    sac_kings1= []
    for i in sac_kings:
        i= ' '.join(map(str, sac_kings))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        sac_kings1.append(i)
    sac_kings1= sac_kings1[0]
    total= 0.0
    for i in sac_kings1.split(" "):
        total+=float(i)
    kings_average= total/len(sac_kings1.split(" "))
    tor_raptors1= []
    for i in tor_raptors:
        i= ' '.join(map(str, tor_raptors))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        tor_raptors1.append(i)
    tor_raptors1= tor_raptors1[0]
    total1= 0.0
    for i in tor_raptors1.split(" "):
        total1+=float(i)
    raptors_average= total1/len(tor_raptors1.split(" "))
    mil_bucks1= []
    for i in mil_bucks:
        i= ' '.join(map(str, mil_bucks))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        mil_bucks1.append(i)
    mil_bucks1= mil_bucks1[0]
    total2= 0.0
    for i in mil_bucks1.split(" "):
        total2+=float(i)
    bucks_average= total2/len(mil_bucks1.split(" "))
    la_clippers1= []
    for i in la_clippers:
        i= ' '.join(map(str, la_clippers))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        la_clippers1.append(i)
    la_clippers1= la_clippers1[0]
    total3= 0.0
    for i in la_clippers1.split(" "):
        total3+=float(i)
    clippers_average= total3/len(la_clippers1.split(" "))
    ny_knicks1= []
    for i in ny_knicks:
        i= ' '.join(map(str, ny_knicks))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        ny_knicks1.append(i)
    ny_knicks1= ny_knicks1[0]
    total4= 0.0
    for i in ny_knicks1.split(" "):
        total4+=float(i)
    knicks_average= total4/len(ny_knicks1.split(" "))
    cle_cavaliers1= []
    for i in cle_cavaliers:
        i= ' '.join(map(str, cle_cavaliers))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        cle_cavaliers1.append(i)
    cle_cavaliers1= cle_cavaliers1[0]
    total5= 0.0
    for i in cle_cavaliers1.split(" "):
        total5+=float(i)
    cavaliers_average= total5/len(cle_cavaliers1.split(" "))
    call= win_percentage()
    cavaliers_percentage= call['Cavaliers']
    knicks_percentage= call['Knicks']
    clippers_percentage= call['Clippers']
    bucks_percentage= call['Bucks']
    kings_percentage= call['Kings']
    raptors_percentage= call['Raptors']
    average_lst= [cavaliers_average, knicks_average, bucks_average, clippers_average, kings_average, raptors_average]
    percentage_lst= [cavaliers_percentage, knicks_percentage, bucks_percentage, clippers_percentage, kings_percentage, raptors_percentage]
    fig, ax = plt.subplots() 
    plt.scatter(average_lst, percentage_lst)
    ax.set_xlabel('PPG', fontsize= 16, color= 'r')
    ax.set_ylabel('Win Percentage', fontsize= 16, color= 'y')
    ax.set_title('Scatterplot of Teams Win Percentage and Highest Scorers PPG')
    plt.xticks(rotation= 90)
    plt.savefig("test.png",bbox_inches='tight')
    matplotlib.pyplot.subplots_adjust(left=None, bottom=0.3, right=None, top=None, wspace=None, hspace=None)
    plt.annotate("Knicks", (8.01, 66))
    plt.annotate("Kings", (14, 71))
    plt.annotate("Cavs", (13, 74))
    plt.annotate("Clippers", (13.5, 58))
    plt.annotate("Raptors", (15.5, 62))
    plt.annotate("Bucks", (18, 53))
    x = np.array(average_lst)
    y = np.array(percentage_lst)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b)
    plt.show()
    return percentage_lst
make_raptors_plot()
final_graph()
def extra_credit_graph():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    var= final_graph()
    cur.execute("SELECT Attendance.homeav FROM Attendance WHERE Attendance.team = 'Kings' AND Attendance.year='2017'")
    kings= cur.fetchall()
    kings_lst= []
    for i in kings:
        i= str(i)
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        kings_lst.append(i)
    cur.execute("SELECT Attendance.homeav FROM Attendance WHERE Attendance.team = 'NY Knicks' AND Attendance.year='2017'")
    knicks= cur.fetchall()
    knicks_lst= []
    for i in knicks:
        i= str(i)
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        knicks_lst.append(i)
    cur.execute("SELECT Attendance.homeav FROM Attendance WHERE Attendance.team = 'Cavaliers' AND Attendance.year='2017'")
    cavs= cur.fetchall()
    cavs_lst= []
    for i in cavs:
        i= str(i)
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        cavs_lst.append(i)
    cur.execute("SELECT Attendance.homeav FROM Attendance WHERE Attendance.team = 'Clippers' AND Attendance.year='2017'")
    clippers= cur.fetchall()
    clippers_lst= []
    for i in clippers:
        i= str(i)
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        clippers_lst.append(i)
    cur.execute("SELECT Attendance.homeav FROM Attendance WHERE Attendance.team = 'Raptors' AND Attendance.year='2017'")
    raptors= cur.fetchall()
    raptors_lst= []
    for i in raptors:
        i= str(i)
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        raptors_lst.append(i)
    cur.execute("SELECT Attendance.homeav FROM Attendance WHERE Attendance.team = 'Bucks' AND Attendance.year='2017'")
    bucks= cur.fetchall()
    bucks_lst= []
    for i in bucks:
        i= str(i)
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        i= i.replace(',', '')
        bucks_lst.append(i)

    attendance_lst= [cavs_lst, knicks_lst, bucks_lst, clippers_lst, kings_lst, raptors_lst]
    fig, ax = plt.subplots() 
    plt.scatter(attendance_lst, var)
    ax.set_xlabel('Attendance', fontsize= 16, color= 'r')
    ax.set_ylabel('Win Percentage', fontsize= 16, color= 'y')
    ax.set_title('Scatterplot of Teams Win Percentage and Fan Attendance')
    plt.xticks(rotation= 90)
    plt.savefig("test.png",bbox_inches='tight')
    matplotlib.pyplot.subplots_adjust(left=None, bottom=0.3, right=None, top=None, wspace=None, hspace=None)
    plt.annotate("Cavs", (20400, 73))
    plt.annotate("Kings", (17500, 72))
    plt.annotate("Knicks", (19700, 66.5))
    plt.annotate("Clippers", (18800, 58))
    plt.annotate("Raptors", (19600, 62))
    plt.annotate("Bucks", (15760, 53))
    plt.show()
    return attendance_lst
extra_credit_graph()
def extra_credit_graph_2():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, 'final.db')
    conn= sqlite3.connect(db)
    cur = conn.cursor() 
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Kings'")
    sac_kings= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Raptors'")
    tor_raptors= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Bucks'")
    mil_bucks= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Clippers'")
    la_clippers= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Knicks'")
    ny_knicks= cur.fetchall()
    cur.execute("SELECT NBA_Stats.PPG FROM NBA_Stats WHERE NBA_Stats.Team = 'Cavaliers'")
    cle_cavaliers= cur.fetchall()
    sac_kings1= []
    for i in sac_kings:
        i= ' '.join(map(str, sac_kings))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        sac_kings1.append(i)
    sac_kings1= sac_kings1[0]
    total= 0.0
    for i in sac_kings1.split(" "):
        total+=float(i)
    kings_average= total/len(sac_kings1.split(" "))
    tor_raptors1= []
    for i in tor_raptors:
        i= ' '.join(map(str, tor_raptors))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        tor_raptors1.append(i)
    tor_raptors1= tor_raptors1[0]
    total1= 0.0
    for i in tor_raptors1.split(" "):
        total1+=float(i)
    raptors_average= total1/len(tor_raptors1.split(" "))
    mil_bucks1= []
    for i in mil_bucks:
        i= ' '.join(map(str, mil_bucks))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        mil_bucks1.append(i)
    mil_bucks1= mil_bucks1[0]
    total2= 0.0
    for i in mil_bucks1.split(" "):
        total2+=float(i)
    bucks_average= total2/len(mil_bucks1.split(" "))
    la_clippers1= []
    for i in la_clippers:
        i= ' '.join(map(str, la_clippers))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        la_clippers1.append(i)
    la_clippers1= la_clippers1[0]
    total3= 0.0
    for i in la_clippers1.split(" "):
        total3+=float(i)
    clippers_average= total3/len(la_clippers1.split(" "))
    ny_knicks1= []
    for i in ny_knicks:
        i= ' '.join(map(str, ny_knicks))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        ny_knicks1.append(i)
    ny_knicks1= ny_knicks1[0]
    total4= 0.0
    for i in ny_knicks1.split(" "):
        total4+=float(i)
    knicks_average= total4/len(ny_knicks1.split(" "))
    cle_cavaliers1= []
    for i in cle_cavaliers:
        i= ' '.join(map(str, cle_cavaliers))
        i= i.replace(',', '')
        i= i.replace('(', '')
        i= i.replace(')', '')
        i= i.replace("'", '')
        cle_cavaliers1.append(i)
    cle_cavaliers1= cle_cavaliers1[0]
    total5= 0.0
    for i in cle_cavaliers1.split(" "):
        total5+=float(i)
    cavaliers_average= total5/len(cle_cavaliers1.split(" "))
    average_lst= [cavaliers_average, knicks_average, bucks_average, clippers_average, kings_average, raptors_average]
    var1= extra_credit_graph()
    fig, ax = plt.subplots() 
    plt.scatter(average_lst, var1)
    ax.set_xlabel('PPG', fontsize= 16, color= 'm')
    matplotlib.pyplot.subplots_adjust(left=0.15, bottom=0.3, right=None, top=None, wspace=None, hspace=None)
    ax.set_ylabel('Attendance', fontsize= 16, color= 'b')
    ax.set_title('Scatterplot of Teams Average PPG and Fan Attendance')
    plt.xticks(rotation= 90)
    plt.savefig("test.png",bbox_inches='tight') 
    plt.annotate("Bucks", (17.5, 16200))
    plt.annotate("Kings", (13.7, 17100))
    plt.annotate("Knicks", (7.7, 19200))
    plt.annotate("Cavs", (12.6, 20000))
    plt.annotate("Clippers", (13, 18500))
    plt.annotate("Raptors", (15.7, 19300))
    plt.show()
extra_credit_graph_2()