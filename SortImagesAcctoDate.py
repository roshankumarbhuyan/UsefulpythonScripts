"""
Created on Sat Sep 29 21:02:08 2018
@author: ROS
"""

from PIL import Image
import os
import shutil
#import random

w_dir = "E:" #Directory to the image folder
dest_dir = "E:\\BACKUP\\sorted_photos" #where to store sorted files.. 
os.chdir(w_dir)
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

#Input is the full path of the images       
def get_date_taken(img):
    if Image.open(img)._getexif() == None:
        return ("0000:00:00 00:00:00")
    else:
        try:
            Image.open(img)._getexif()[36867]
            dat= Image.open(img)._getexif()[36867]     
            return (dat)
        except:
            return ("0000:00:00 00:00:00")
        
def create_folder(img):
    dat = get_date_taken(img)
    y= dat[0:4]
    m= dat[5:7]
    name= y + "-" + m
    path = os.path.join(dest_dir, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return(path)


def move_files(file):
    if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg"):
        path_fol = create_folder(file)
        name = get_date_taken(file)
        z= get_date_taken(file)[0:4] + "-" + name[5:7]
        file_name = os.path.basename(path)
        check = os.path.join(path_fol,file_name)
        if os.path.exists(check) :
            print(file_name + " Already Exists in"  + check + "Skipping")
            pass
        else:
            a= "Moving {0} to {1}"
            print(a.format(file,z))
            shutil.move(file, path_fol)
    else:
         pass

move_files(w_dir)

for folderName, subfolders, filenames in os.walk(w_dir):
    print('The current folder is ' + folderName)
    for file in os.listdir(folderName):
        print("The current file is", file)
        path = os.path.join( folderName ,file)
        move_files(path)         
         
