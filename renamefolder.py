import os
basedir = os.getcwd()+ "/image/" 
for fn in os.listdir(basedir):
	count=0
	for filename in os.listdir( basedir+ fn):
		print(filename)

	#print(fn)
	a = fn.rpartition('-')
	s = a[2]
	z = s.lower()
	print(s)
	print(z)
	os.rename(fn,z)

 # if not os.path.isdir(os.path.join(basedir, fn)):
 #   continue # Not a directory
  #if not '-' in fn:
   # continue # Already in the correct form
  #if '-' in fn:
   # continue # Invalid format
  #a = fn.rpartition('-')
  #os.rename(os.path.join(basedir, fn),
   #         os.path.join(basedir,a[2]))