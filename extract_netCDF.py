from netCDF4 import Dataset
import numpy as np

# Reading in the netCDF file
data = Dataset(r'D:\ScientificPython\NetCDF_with_Python\netCDF_Temperature\1961.nc','r')
#print(data)
#print(type(data))

# Displaying variable names in the netCDF files
#print(data.variables.keys())

# Accesing the variables (lon, lat, time, tave, rstn)

# get some information about the longitude variable
lon = data.variables['lon']
#print(lon)
# make use of the long_name attribute to print the full name
#print(lon.long_name)

# Repeat the above for latitude
lat = data.variables['lat']
#print(lat.long_name)

# Repeat the above for time
time = data.variables['time']
#print(time)

# Repeat the above for average temperature
tave = data.variables['tave']
#print(tave)

# Repeat the above for rstn
rstn = data.variables['rstn']
#print(rstn)
# rstn is the ratio of 0.5deg-grids with station, we are not interested in this variable

# Check out dimensions
#print(lon.dimensions)
#print(lat.dimensions)
#print(time.dimensions)
#print(tave.dimensions)

# Acessing the data from the variables
time_data = data.variables['time'][:]
print(time_data)

lon_data = data.variables['lon'][:]
print(lon_data)

lat_data = data.variables['lat'][:]
print(lat_data)