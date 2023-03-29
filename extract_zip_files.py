import patoolib
import os

for zipfile in os.listdir(r'D:\ScientificPython\NetCDF_with_Python'):
    # print(zipfile)  # lists all the files in the folder
    if zipfile[-3:] == '.gz':
        # print(zipfile) # Check it lists only ******.gz files
        patoolib.extract_archive(zipfile, outdir=r'D:\ScientificPython\NetCDF_with_Python\netCDF_Temperature')

# patool extracted files does not add the .nc file extension
# Add .nc extension to the extracted files

for extracted_file in os.listdir(r'D:\ScientificPython\NetCDF_with_Python\netCDF_Temperature'):
    # Change the current working directory for saving the files in the required directory
    os.chdir(r'D:\ScientificPython\NetCDF_with_Python\netCDF_Temperature')
    os.rename(extracted_file, extracted_file + '.nc')

