import os
basedir = os.getcwd()+ "/stanford" 
for fn in os.listdir(basedir):
	count=0
	print(fn)
	a = fn.rpartition('-')
	s = a[2]
	z = s.lower()
	print(s)
	print(z)
	old_name = basedir + "/" + fn
	new_name = basedir + "/" + z
	os.rename(old_name,new_name)

 # if not os.path.isdir(os.path.join(basedir, fn)):
 #   continue # Not a directory
  #if not '-' in fn:
   # continue # Already in the correct form
  #if '-' in fn:
   # continue # Invalid format
  #a = fn.rpartition('-')
  #os.rename(os.path.join(basedir, fn),
   #         os.path.join(basedir,a[2]))