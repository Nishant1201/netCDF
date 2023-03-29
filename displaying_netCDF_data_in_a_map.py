from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
plt.rcParams['pcolor.shading'] = 'auto'  # to avoid warnings in color scheme (line 25)

# Loading the data
data = Dataset(r'D:\ScientificPython\NetCDF_with_Python\display_netCDF_data_on_map\1962.nc')
#print(data)
#print(data.variables)
#print(data.variables.keys())

lats = data.variables['lat'][:]
lons = data.variables['lon'][:]
time = data.variables['time'][:]
tave = data.variables['tave'][:]

# Create a variable mp (map) using Basemap
mp = Basemap(projection='merc', llcrnrlon=63.29590487394516, llcrnrlat=5.038228576233911,
            urcrnrlon=99.59473325017883, urcrnrlat=38.369077058122876, resolution='i')
lon, lat = np.meshgrid(lons, lats)
x, y = mp(lon, lat)

# create a color scheme
c_scheme = mp.pcolor(x,y,np.squeeze(tave[0,:,:]),cmap='jet')  # tave[time,lat,lon] time 0 corresponds to day 1
# draw the coastline, states and countries
mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()

# specifying a color bar
cbar = mp.colorbar(c_scheme, location='right', pad='10%')

plt.title('Averaged temperature on 01-01-1962')
plt.show()
