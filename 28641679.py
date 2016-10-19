#!/usr/bin/python
import csv
import sys
import datetime
from pylab import *
from matplotlib.ticker import MaxNLocator

date      = []
Median    = []
Upper     = []
Lower     = []

inp           = open('28641679.csv','rU')
try:
    reader = csv.reader(inp)
    for row in reader:
        print(row)
        Init_Date = row[0]
        if(Init_Date[0:3] == 'Jan'):   Month = 1
        elif(Init_Date[0:3] == 'Feb'): Month = 2
        elif(Init_Date[0:3] == 'Mar'): Month = 3
        elif(Init_Date[0:3] == 'Apr'): Month = 4
        elif(Init_Date[0:3] == 'May'): Month = 5
        elif(Init_Date[0:3] == 'Jun'): Month = 6
        elif(Init_Date[0:3] == 'Jul'): Month = 7
        elif(Init_Date[0:3] == 'Aug'): Month = 8
        elif(Init_Date[0:3] == 'Sep'): Month = 9
        elif(Init_Date[0:3] == 'Oct'): Month = 10
        elif(Init_Date[0:3] == 'Nov'): Month = 11
        else: Month = 12

        day  = Init_Date[4:6]
        year = Init_Date[-3:-1]

        Median.append( float(row[1]) )
        Upper.append( float(row[2]) )
        Lower.append( float(row[3]) )

        dates = str(Month) + '/' + str(day).strip() + '/' + str(year)
        print(dates)
        date.append(datetime.datetime.strptime(dates,'%m/%d/%y'))
finally:
    inp.close()

fig, plt = plt.subplots()
matplotlib.rc('xtick',labelsize=18)
matplotlib.rc('ytick',labelsize=18)
x = date
y = Median
y1 = Upper
y2 = Lower

print(x)
print(y)
print(y1)
print(y2)

plt.set_xlabel(r'$Date$',fontsize = 18)
plt.set_ylabel(r'$Y-Value$',fontsize = 18)
plt.plot(x, y1, color = 'red')
plt.plot(x, y2, color = 'red')
plt.fill_between(x,y2,y1,interpolate=True,color='red')
plt.plot(x, y, color = 'black')
plt.xaxis.set_major_locator(MaxNLocator(nbins = 12))
fig.savefig("Test.png")