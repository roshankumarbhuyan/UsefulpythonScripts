import image_slicer as slicer
import os, sys

basedir = os.getcwd()

for fn in os.listdir(basedir):
	print(fn)
	slicer.slice(fn, 6)