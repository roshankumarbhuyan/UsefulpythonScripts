import os

basedir = os.getcwd()

for fn in os.listdir(basedir):
	z = os.path.getsize(fn)
	#print("The size of %s is %d " %(fn, z) ) 
	if z > 1700000:
		print("the size of %s is %d "%(fn,z) )
		print("removing %s " %(fn))
		os.remove(fn)