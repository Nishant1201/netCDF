from pathlib import Path
import imageio

image_path = Path('Images')  # Path from where the images will be read

# The glob module, which is short for global, is a function that's used 
# to search for files that match a specific file pattern or name.
images = list(image_path.glob('*.png'))  # imageio library supports various image formats including jpg, png
# print(images)   # print the image name for checking

# Read the images by using the imread() method from imageio
# imread() method will create a numpy array for each image with its RGBA values read
# All of these images will be saved to a list called image_list

image_list = []

for file_name in images:
    image_list.append(imageio.imread(file_name))

# After you’re done with reading your images, 
# you can simply check if all images have been read as they’re supposed by running 
# len(image_list), which should match the number of PNG files in the folder.
print(len(image_list)) 

# Create the animated image using the mimwrite() method
imageio.mimwrite('Temperature.gif',image_list)

