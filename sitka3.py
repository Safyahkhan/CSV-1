# using the datetime module
# adding dates to the x axis for the month of July


import csv
from datetime import datetime
import matplotlib.pyplot as plt


infile = open("sitka_weather_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile) #it makes the list of the header

for index, column_header in enumerate(header_row): #it gives you the location(index value) and value of the record, it only works with lists
    print(index,column_header)

highs = []
dates = []
lows = []
#mydate = datetime.strptime('2018-07-01', '%y=%m=%d')


for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(thedate)
#print(highs)



fig = plt.figure()

plt.plot(dates,highs, c='red', alpha=0.5) # plot creates a line graph
plt.plot(dates,lows, c='purple', alpha=0.5)
plt.fill_between(dates,highs,lows, facecolor="grey", alpha=0.6)
plt.title("Daily and low high temperatures - 2018", fontsize=16)
plt.xlabel("Dates", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis= 'both', which='major', labelsize=12)

fig.autofmt_xdate()

#plt.show() commented out this for the 16th march assignment

#How to do suplots

plt.subplot(2,1,1)
plt.plot(dates,highs,c='red')
plt.title("Highs")

print('\n')

plt.subplot(2,1,2)
plt.plot(dates,lows, c='blue')
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")
plt.show()