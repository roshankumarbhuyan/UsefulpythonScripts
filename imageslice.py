import image_slicer as slicer
import os, sys

basedir = os.getcwd()
img_dir = os.path.join(basedir, "jpg")
os.chdir(img_dir)
for fn in os.listdir(img_dir):
	print(fn)
	slicer.slice(fn, 6)
