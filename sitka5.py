import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Open and read the Sitka file
with open("sitka_weather_2018_simple.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Find the indexes for TMIN, TMAX and NAME columns
    tmax_index = header_row.index("TMAX")
    tmin_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")
    
    # Create lists to store the data
    highs = []
    dates = []
    lows = []
    name = ""
    
    for row in reader:
        # Store the name of the station
        name = row[name_index]
        
        # Store the data for highs, lows and dates
        high = int(row[tmax_index])
        low = int(row[tmin_index])
        thedate = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        lows.append(low)
        dates.append(thedate)
        

# Open and read the Death Valley file
with open("death_valley_2018_simple.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Find the indexes for TMIN, TMAX and NAME columns
    tmax_index = header_row.index("TMAX")
    tmin_index = header_row.index("TMIN")
    name_index = header_row.index("NAME")
    
    # Create lists to store the data
    dv_highs = []
    dv_dates = []
    dv_lows = []
    dv_name = ""
    
    for row in reader:
        # Store the name of the station
        dv_name = row[name_index]
        
        # Store the data for highs, lows and dates
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
            thedate = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dv_highs.append(high)
            dv_lows.append(low)
            dv_dates.append(thedate)
        

# Plot the data
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))

# Plot the Sitka data
ax1.plot(dates, highs, c='red', alpha=0.7)
ax1.plot(dates, lows, c='blue', alpha=0.7)
ax1.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
ax1.set_title(f"{name}")
#ax1.set_xlabel("Dates")
#ax1.set_ylabel("Temperature(F)")
ax1.tick_params(axis='both', which='major', labelsize=12)

# Plot the Death Valley data
ax2.plot(dv_dates, dv_highs, c='red', alpha=0.7)
ax2.plot(dv_dates, dv_lows, c='blue', alpha=0.7)
ax2.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.2)
ax2.set_title("Death Valley, CA US")
#ax2.set_xlabel("Dates")
#ax2.set_ylabel("Temperature(F)")
ax2.tick_params(axis='both', which='major', labelsize=12)

# Set the title of the entire figure
fig.suptitle(f"Temperature comparison between {name} and {dv_name}")

# Rotate the x-axis labels
fig.autofmt_xdate()

plt.show()
