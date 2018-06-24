# @author Leonie Kruger
# @project ELEN 7046

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
import numpy as np

import csv

x = []
y = []

with open('/Users/leoniekruger/CencusData/Data/population_growth_sa.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
print(x)
print(y)
coef = np.polyfit(x, y, 1)
p_func = np.poly1d(coef)
xp = np.linspace(x[0], x[len(x)-1]+20, 100)

ax = plt.gca()
ax.set_facecolor((0.898, 0.898, 0.898))
pylab.title('Population Growth Linear Fit')
ax.set_xlabel("Year", fontdict=None, labelpad=None)
ax.set_ylabel("Population in Millions", fontdict=None, labelpad=None)
plt.plot(x, y, '.', xp, p_func(xp))
plt.show()