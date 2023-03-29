from netCDF4 import Dataset
import numpy as np

# Reading in the netCDF file
data = Dataset(r'D:\ScientificPython\NetCDF_with_Python\netCDF_Temperature\1961.nc','r')

# storing the lat and lon data into variables
lat = data.variables['lat'][:]
#print(type(lat))
lon = data.variables['lon'][:]
#print(type(lon))

# Go to Google Maps and get latitude and longitude of Kathmandu
lat_kathmandu, lon_kathmandu = 27.710475687929982, 85.33196862778622

# Squared difference of lat and lon (to avoid negative values)
sq_diff_lat = (lat - lat_kathmandu)**2.
sq_diff_lon = (lon - lon_kathmandu)**2.

# Identifying the index of the minimum value for lat and lon
min_index_lat = sq_diff_lat.argmin()
min_index_lon = sq_diff_lon.argmin()
# let's verify it
#print(sq_diff_lat[min_index_lat], sq_diff_lat.min())
#print(sq_diff_lon[min_index_lon], sq_diff_lon.min())

# Let us extract the temperature data into a variable
temp = data.variables['tave']
#print(temp)
# printing the temperature data on the first day
#print(temp[0,min_index_lat,min_index_lon])
#print(temp[5,min_index_lat,min_index_lon], temp.units)  # prints units along with value
#print(temp[364,min_index_lat,min_index_lon],temp.units)

# Extract the dates from netCDF files
# get the units for time
#print(data.variables['time'].units)
#print(data.variables['time'].units[14:24])
# get the starting and ending date
starting_date = data.variables['time'].units[14:24]
ending_date = data.variables['time'].units[14:18] + '-12-31'  # last day of the corresponding year
#print(starting_date, ending_date)

# Create a date range with pandas
import pandas as pd
date_range = pd.date_range(start = starting_date, end = ending_date)
#print(date_range)
# Create an empty (filled with zeros) pandas dataframe
df = pd.DataFrame(0, columns=['Temperature'], index=date_range)  # Filled with 0 for illustration

# Create a numpy array with same dimensions as time variable
#print(data.variables['time'])
dt = np.arange(0,data.variables['time'].size) # this will account for leap years too through the size (365/366)

for time_index in dt:
    df.iloc[time_index] = temp[time_index, min_index_lat, min_index_lon]

#print(df)

# Save the time series data to a csv file
df.to_csv('Temperature_Kathmandu.csv')