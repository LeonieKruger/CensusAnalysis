# libraries
import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.cm as cm

# see https://matplotlib.org/examples/color/colormaps_reference.html for colour map colours
# @author Leonie Kruger
# @project ELEN 7046

type_of_crime = []
province = []
number_occurence =[]

csvfile = open("/Users/leoniekruger/CencusData/Data/CrimeNumberProvince.csv", "r")
csvReader = csv.reader(csvfile)





with open('/Users/leoniekruger/CencusData/Data/CrimeNumberProvince.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
            province.append(row[0])
            type_of_crime.append(row[1])
            number_occurence.append(int(row[2]) * 10)
        # y.append(float(row[1]))

# create data

colors=cm.cool(np.random.rand(10))

# Use those colors as the color argument
plt.scatter(province, type_of_crime, s=number_occurence, color=colors)

# Add titles (main and on axis)

plt.xlabel("Province")
plt.ylabel("CrimeType")
plt.title("Crime South Africa")

plt.show()
