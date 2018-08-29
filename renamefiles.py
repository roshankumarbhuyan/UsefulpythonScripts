import os, sys

#for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
# base_file, ext = os.path.splitext(filename)

basedir = os.getcwd() + "/small"
count = 0
for fn in os.listdir(basedir):
	img_path = basedir + '/' + fn
	newname = basedir + '/' + '%s_%d.png'%("field",count)
	os.rename(img_path,newname)
	print(newname)
	count += 1