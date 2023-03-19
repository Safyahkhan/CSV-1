import csv

infile = open("sitka_weather_07-2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile) #it makes the list of the header

for index, column_header in enumerate(header_row): #it gives you the location(index value) and value of the record, it only works with lists
    print(index,column_header)

highs = []


for row in csvfile:
    highs.append(int(row[5]))
print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(highs, c='red') # plot creates a line graph
plt.title("Daily high temp for Sitka Alaska July 2018", fontsize=16)
plt.xlabel("Dates", )
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis= 'both', which='major', labelsize=16)

fig.autofmt_xdate()

plt.show()