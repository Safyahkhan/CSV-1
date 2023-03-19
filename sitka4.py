# using the datetime module
# adding dates to the x axis for the month of July


import csv
from datetime import datetime
import matplotlib.pyplot as plt


infile = open("death_valley_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile) #it makes the list of the header
print(header_row)


for index, column_header in enumerate(header_row): #it gives you the location(index value) and value of the record, it only works with lists
    print(index,column_header)

highs = []
dates = []
lows = []
#mydate = datetime.strptime('2018-07-01', '%y=%m=%d')


for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {row[2]}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)


    
#print(highs)


fig = plt.figure()

plt.plot(dates,highs, c='red', alpha=0.6) # plot creates a line graph, alpha is the intensity 
plt.plot(dates,lows, c='purple', alpha=0.6)
plt.fill_between(dates,highs,lows, facecolor="grey", alpha=0.3)
plt.title("Daily and low high temperatures - 2018", fontsize=16)
plt.xlabel("Dates", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis= 'both', which='major', labelsize=12)

fig.autofmt_xdate()

plt.show()


