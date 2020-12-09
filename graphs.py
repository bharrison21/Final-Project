import matplotlib
import matplotlib.pyplot as plt 
#data for plotting
y= [26.3, 24.4, 20.1, 16.8, 25.7]
# d= ["Bulls", "Knicks", "Mavericks", "Nets", "76ers"]
# fig, ax = plt.subplots()
# #create the bar graph
# plt.bar(d, y)
# ax.set(xlabel= 'Team', ylabel= 'Offensive points per game', title= 'PPG per NBA team for the 2018 season')
# #save
# plt.show()

fan_attendance= [62000, 54000, 43000, 39000, 58000]
fig, ax= plt.subplots()
plt.xlabel('fan_attendance', fontsize= 14, color= 'red')
plt.scatter(y, fan_attendance)
ax.plot(xlabel= 'PPG', ylabel= 'Fan Attendance', title= 'Scatterplot of PPG and Fan Attendance for the 2018 NBA Season')
plt.show()