# Script for Dropbox functions: 
	# (1) Check dropbox for new image files 
	# (2) Download new image files and redownload CSV of relevant image information



# Use module os, use Terminal, use cd to change to (or input: what is the path to the dropbox)

# Change working directory to Dropbox

import os
import glob

path = '/Users/nicolekim/Dropbox'

dirpath = os.getcwd()
print("Current working directory %s" % dirpath)

os.chdir(path)
# Check current working directory.
dirpath = os.getcwd()

print("Directory changed successfully %s" % dirpath)

testpath = '/Users/nicolekim/Dropbox/20180410175530.npy'



## Function: Check dropbox for new image files and if yes, download new images files and redownload CSV


# The timestamp of the last image detected by the Master script (type = integer)
last_image = 20180410175529 # test sample

for file in glob.glob("*.npy"):
    name = file.split('.') # file is the name of the file, split into timestamp + .npy (type = string)
    filename = name[0]
    timestamp = int(filename) 
    if timestamp > last_image: # is file is more recent than the last image detected by Master script?
    	# download .npy file
    	imagearray = file 
    	# last_im = timestamp # reset the timestamp of the last image
    	print(imagearray)
    	

# mastercsv = 'Name of CSV Here' # resave csv as mastercsv (everytime so previous csv file overwritten)



# Code for seeing whether a file exists, output of os.path.isfile is a boolean
# val = os.path.isfile('20180410175530.npy') 
# print(val)


