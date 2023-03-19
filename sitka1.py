# using the datetime module
# adding dates to the x axis for the month of July


import csv
from datetime import datetime
import matplotlib.pyplot as plt


infile = open("sitka_weather_07-2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile) #it makes the list of the header

for index, column_header in enumerate(header_row): #it gives you the location(index value) and value of the record, it only works with lists
    print(index,column_header)

highs = []
dates = []
#mydate = datetime.strptime('2018-07-01', '%y=%m=%d')


for row in csvfile:
    highs.append(int(row[5]))
    thedate = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(thedate)
#print(highs)



fig = plt.figure()

plt.plot(dates,highs, c='red') # plot creates a line graph
plt.title("Daily high temp for Sitka Alaska July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis= 'both', which='major', labelsize=12)

fig.autofmt_xdate()

plt.show()