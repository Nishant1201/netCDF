# netCDF
Handling netCDF files with Python for data visualization

Part 1 (Download Temperature and Precipitation Data in netCDF)
http://aphrodite.st.hirosaki-u.ac.jp/download/
http://aphrodite.st.hirosaki-u.ac.jp/download/create/

Part 2 (Automating Bulk netCDF File Download Process using Python)
Code - bulk_download_netCDF.py (Downloads the compressed .gz files into the current folder)

Extract all the .gz files into another folder "netCDF_Temperature" by writing a Python script extract_zip_files.py
patool library is useful for extracting .gz files. Install patool as below
Install patool - pip install patool (works)
			conda install patool (might not work)


Install panoply - https://www.giss.nasa.gov/tools/panoply/download/
Open panoply and plot the t_ave for a year (for example, 1964)
Panolply is not able to do arithmetic operations, it is just for the visualization purposes

Part 3 (Extracting time series data from a netCDF file into a CSV)
3.1 - Introduction to accessing variables and data from the netCDF file
3.2 - Python script for extracting the data into a csv file

Install netCDF4 
https://pypi.org/project/netCDF4/  - pip install netCDF4
https://anaconda.org/conda-forge/netcdf4 - conda install -c conda-forge netcdf4

Code - 1. extract_netCDF.py
	 2. extract_netCDF_Time_Series.py

Part 4 (How to Plot netCDF data onto a Map using Python (with Matplotlib Basemap toolkit))
Code - displaying_netCDF_data_in_a_map

Install Matplotlib Basemap Toolkit API

Open Anaconda prompt and run the following commands as administrator,
python -m pip install basemap
python -m pip install basemap-data
python -m pip install basemap-data-hires

Mercator projection - The Mercator projection is a cylindrical map projection presented by Flemish geographer and cartographer Gerardus Mercator in 1569. It became the standard map projection for navigation because it is unique in representing north as up and south as down everywhere while preserving local directions and shapes.


Part 5 (How to create an animated time-lapse of temperature using netCDF grid data)
pip install imageio
pip install imageio-ffmpeg
pip install pygifsicle
