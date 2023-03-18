import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename1 = "death_valley_2018_simple.csv"
filename2 = "sitka_weather_2018_simple.csv"

def get_title(filename):
    station_name = filename.split("_")[0].title()
    return f"Highs and Lows of {station_name}"

def get_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # get index positions for the data
        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')

        # get data from each row
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                date = datetime.strptime(row[date_index], '%Y-%m-%d')
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {row[date_index]}")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows

# get data for both files
dates1, highs1, lows1 = get_data(filename1)
dates2, highs2, lows2 = get_data(filename2)

# create subplots
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
fig.suptitle(get_title(filename1), fontsize=16)

# plot data on each axis
ax1.plot(dates1, highs1, c='red', alpha=0.5)
ax1.plot(dates1, lows1, c='purple', alpha=0.5)
ax1.fill_between(dates1, highs1, lows1, facecolor="grey", alpha=0.1)
ax1.set_title("Death Valley", fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)

ax2.plot(dates2, highs2, c='red', alpha=0.5)
ax2.plot(dates2, lows2, c='blue', alpha=0.5)
ax2.fill_between(dates2, highs2, lows2, facecolor="grey", alpha=0.1)
ax2.set_title("Sitka", fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)

# set common labels and formatting
fig.autofmt_xdate()
plt.xlabel("Dates", fontsize=12)
plt.ylabel("Temperature(F)", fontsize=12)

plt.show()
