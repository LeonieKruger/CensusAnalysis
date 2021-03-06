# @author Leonie Kruger
# @project ELEN 7046

import urllib
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pip._vendor import certifi
import csv
import matplotlib.cm as cm

colors=cm.cool(np.random.rand(10))
i=0

m = Basemap(projection='mill',llcrnrlat=-35,urcrnrlat=-20,
            llcrnrlon=13,urcrnrlon=35,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#996600', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

# See https://www.w3schools.com/colors/colors_picker.asp for colours



type_of_crime = []
province = []
number_occurence =[]
lons=[]
lats=[]

csvfile = open('/Users/leoniekruger/CencusData/Data/HouseBreaking.csv', "r")
csvReader = csv.reader(csvfile)

with open('/Users/leoniekruger/CencusData/Data/HouseBreaking.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        province.append(row[0])
        number_occurence.append(int(row[2]) * 10)

for province in province:
    from geopy.geocoders import Nominatim
    def uo(args, **kwargs):
            return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)
    geolocator = Nominatim()
    geolocator.urlopen = uo
    location = geolocator.geocode(province+ " , South Africa")
    print(location.address)
    print((location.latitude, location.longitude))
    lat = location.latitude
    lon = location.longitude
    x,y = m(lon,lat)
    m.plot(x, y,'go', markersize=number_occurence[i] / 100)
    i=i+1

plt.title('House Breaking Plotting')
plt.show()