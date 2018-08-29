import os, sys

#for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
# base_file, ext = os.path.splitext(filename)

basedir = os.getcwd() + "/stanford"
for fn in os.listdir(basedir):
	print(fn)
	count=0
	subdir = basedir + '/' + fn  + '/'
	for filename in os.listdir(subdir):
		img_path = subdir + '/' + filename
		newname = subdir + '/' + '%s_%d.jpg'%(fn,count)
		os.rename(img_path,newname)
		print(newname)
		count += 1