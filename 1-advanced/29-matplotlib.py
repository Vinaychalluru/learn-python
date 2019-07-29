import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import dates as mdates

import numpy as np
from datetime import datetime as dt

x = [ n for n in range(10)]
y = [ n**2 for n in range(10) ]
z = [ n*5 for n in range(10) ]

plt.plot(x, y, color='k')
plt.scatter(x, z, s=10, c=z, cmap='Blues')

# Filling space between data sets
plt.fill_between(x, y, z, facecolor='blue', alpha=0.25)

plt.title("Number Squares")
plt.xlabel("Number")
plt.ylabel("Value")
plt.tick_params(axis='both', which='major',labelsize=11)

plt.axes().get_yaxis().set_visible(False)

plt.legend()
plt.show()

# Plotting High Daily Temperatures
dates = [dt(2016, 6, 21), dt(2016, 6, 22),dt(2016, 6, 23), dt(2016, 6, 24)]
highs = [57, 68, 64, 59]
fig = plt.figure(dpi=128, figsize=(7,5))

plt.plot(dates, highs, c='red')
plt.title("Daily High Temps", fontsize=24)
plt.ylabel("Temp (F)", fontsize=16)

x_axis = plt.axes().get_xaxis()
x_axis.set_major_formatter(mdates.DateFormatter('%B %d %Y'))
fig.autofmt_xdate()
plt.show()