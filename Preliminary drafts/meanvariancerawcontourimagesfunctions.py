
import os
import glob
import numpy as np

# f= open(filename,'r')
# line = f.readline() 
# Script for Dropbox functions: 
	# (1) Check dropbox for new image files 
	# (2) Download new image files and redownload CSV of relevant image information
# Use module os, use Terminal, use cd to change to (or input: what is the path to the dropbox)
# Change working directory to Dropbox
# f= open(filename,'r')
## Function: Check dropbox for new image files and if yes, download new images files and redownload CSV

# The timestamp of the last image detected by the Master script (type = integer)
#last_image = 20180410175529 --> test sample

def getrawImage():
	path = '/Users/nicolekim/Dropbox'
	dirpath = os.getcwd() #current dir. 
	#print("Current working directory %s" % dirpath)
	if dirpath != path 
	os.chdir(path)#cgange directory
	# Check current working directory.
	dirpath = os.getcwd()#update to dropbox directory
	print("Directory changed successfully %s" % dirpath)
	for file in glob.glob("*.npy"): 
    	name = file.split('.') # file is the name of the file, split into timestamp + .npy (type = string)
    	filename = name[0]
    	timestamp = int(filename) 
    	if timestamp > last_image: # is file is more recent than the last image detected by Master script?
    	# download .npy file
    		image_path = os.path.join(dirpath, file)
    		image_array = np.load(image_path)
    	return image_array

def getImagecontourdata():
	path = '/Users/nicolekim/Dropbox'
	dirpath = os.getcwd() #current dir. 
	#print("Current working directory %s" % dirpath)
	os.chdir(path)#cgange directory
	# Check current working directory.
	if dirpath != path 
	dirpath = os.getcwd()#update to dropbox directory
	print("Directory changed successfully %s" % dirpath)
	for file in glob.glob("*.npy"): 
    	name = file.split('.') # file is the name of the file, split into timestamp + .npy (type = string)
    	filename = name[0]
    	timestamp = int(filename) 
    	if timestamp > last_image: # is file is more recent than the last image detected by Master script?
    	# download .npy file
    		image_path = os.path.join(dirpath, file)
    		contourimage_array = np.load(image_path) 
    	return contourimage_array


def getMeanVariance():
	path = '/Users/nicolekim/Dropbox'
	dirpath = os.getcwd() #current dir. 
	print("Current working directory %s" % dirpath)
	os.chdir(path)#cgange directory
# Check current working directory.
	dirpath = os.getcwd()#update to dropbox directory
	print("Directory changed successfully %s" % dirpath)
	csvpath = '/Users/nicolekim/Dropbox/CSV-FILE-NAME' ## ADJUST THIS
	with open('csvpath') as f:
			mastercsv = 'Name of WebcamTeam CSV Here' # resave csv as mastercsv (everytime so previous csv file overwritten)
			reader = csv.reader(f) #csv.reader(f) takes down each line and makes a list of all the objects inside each line.  
			meanRGB = []
			varianceRGB = []
			for rownumber, rowcontent in enumerate(reader): 
				lastrownumber = sum(1 for row in fileObject)
				if rownumber == lastrownumber
					 meanRGB = rowcontent[2:5]
					 varianceRGB = rowcontent[5:]
			return meanRGB, varianceRGB



# Code for seeing whether a file exists, output of os.path.isfile is a boolean
# val = os.path.isfile('20180410175530.npy') 
# print(val)
#f.close()
#csv file . 7 colmns . first colum = name . mean r , mean g, mean b, var r, var  g , var b

