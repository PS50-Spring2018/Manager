# Script for Dropbox functions: 
	# (1) Check dropbox for new image files 
	# (2) Download new image files and redownload CSV of relevant image information



# Use module os, use Terminal, use cd to change to (or input: what is the path to the dropbox)

# Change working directory to Dropbox

import os
import glob
import numpy as np

# still need to figure out specifics for when this isn't being used on my (Nicole's) computer
def changedirectory():
	path = '/Users/nicolekim/Dropbox'

	dirpath = os.getcwd()
	print("Current working directory %s" % dirpath)

	os.chdir(path)
	# Check current working directory.
	dirpath = os.getcwd()

	print("Directory changed successfully %s" % dirpath)

	csvname = 'summary.csv' 
	csvpath = os.path.join(dirpath, csvname)

##Function: Check dropbox for new image files and if yes, download new images files and redownload CSV

# The timestamp of the last image detected by the Master script (type = integer)
last_image = 20180410175529 # test sample

def filecheck():
	for file in glob.glob("*.npy"):
    	if 'c' in file:
        	break
    	name = file.split('.') # file is the name of the file as a list of 2 elements, split into timestamp + .npy (type = str)
    	timestamp_str = name[0]
    	file_c = str(timestamp_str + 'c.npy') # name of image with contour (type = str)
    	timestamp_int = int(timestamp_str)
    	if timestamp_int > last_image: # is file is more recent than the last image detected by Master script? (both variables are type = int)
        	# download .npy file
        	image_path = os.path.join(dirpath, file) # path to raw image
        	imagec_path = os.path.join(dirpath, file_c) # path to image with contour
        	image_array = np.load(image_path) # contains the np array of image
        	image_arrayc = np.load(imagec_path) # contains np array of image with contour
        	# redownload the csv of means and variances
        	mastercsv = open(csvpath, 'r')
        	templist = []
        	for line in mastercsv:
        	    templist.append(line)
        	print(templist[-1])
        	data = templist[-1].split(',') # grab the last line of the csv, split into constitute parts
        	mean_array = [float(data[1]), float(data[2]), float(data[3])] # array of mean RGB values
        	var_array = [float(data[4]), float(data[5]), float(data[6])] # array of variance of RGB values
        	fulldata = []
            fulldata.append(mean_array)
            fulldata.append(var_array)
            fulldata.append(image_array)
            fulldata_array = np.array(fulldata)

        	mastercsv.close()
        	# reset last_image value to the last image worked with
        	# UNCOMMENT THIS WHEN READY TO TEST MORE THAN 1 IMAGE: 
        	last_image = timestamp_int


# Code for seeing whether a file exists, output of os.path.isfile is a boolean
# val = os.path.isfile('20180410175530.npy') 
# print(val)


