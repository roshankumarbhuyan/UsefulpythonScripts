import image_slicer 
import os
base = "C:/Users/ROS/Desktop/Sorted_photos"
os.chdir(base)
for items in os.listdir(base):
	print(items)
	if items.endswith(".png"):
		tiles = image_slicer.slice(items, 9, save=False)
		image_slicer.save_tiles(tiles, directory='C:\\Users\\ROS\\Desktop\\Sorted_photos\\Ros',\
                            prefix=items)
