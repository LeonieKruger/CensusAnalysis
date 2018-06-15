# @author Leonie Kruger
# @project ELEN 7046

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
import numpy as np


from scipy.optimize import curve_fit
import plotly

import csv

x = []
y = []

with open('/Users/leoniekruger/python/population_growth_sa.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

def exponenial_func(x, a, b):
    return a*np.exp(b*x)


popt, pcov = curve_fit(exponenial_func, x, y,p0=(24,0.005),maxfev=1000)

xx = np.linspace(1955,2018,10)
yy = exponenial_func(xx, *popt)

plt.plot(x,y,'o', xx, yy)
pylab.title('Exponential Fit')
ax = plt.gca()
ax.set_facecolor((0.898, 0.898, 0.898))
fig = plt.gcf()
py.plot_mpl(fig, filename='Exponential-Fit-with-matplotlib')