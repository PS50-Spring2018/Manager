
# import a library that has code to take pictures 
import os
# import a library that has a function that can return a list of path names that match the inputed pathname
import glob
# import numpy library for its ability to work with arrays, list, can list images as arrays, etc. 
import numpy as np
# import the csv libary because we are familar with comma seperated value data sets. We will be working with a csv when the webcam interface team submits 
# the average means and variances of Red, Green, and Blue per each image.
import csv

#import the sys module to gain access to some variables used or maintained by the interpreter
import sys
sys.path.append('/Users/nicolekim/Desktop/PS50/repo/DataAnalysis')
from dashboard_function import dashboard # Data Analysis dashboard plot function

# import a library that will have a function that allows the code to run every so many seconds. 
import time

# A function that accesses the dropbox application in the Manager team's computer and obtains two files for each image: the image the os code took and a
# csv file with the average means and variances of Red, Green, and Blue per each image (each image is on a different line within the csv file).
def getdropbox():
	"""Checks dropbox and updates list of timestamps as integers.
	Note: Assumes we're inside the dropbox directory.
	Returns:
	========
	lst_of_TS : list of timestamps (as integers not filenames)
	"""
# initiate a variable that will be a list of all the timestamps of the files to keep a track on when there is an update. 
	lst_of_TS = []
# Need a for loop that will go through the files in the path and check to see for numpy files. 
	for file in glob.glob("*.npy"):

		#print(file)
		name = file.split('.') # file is the name of the file as a list of 2 string elements
		timestamp_str = name[0] # grab the timestamp portion of the file name
		timestamp_int = int(timestamp_str) # convert the timestamp into an integer
		lst_of_TS.append(timestamp_int) # add the timestamp integer to the list 
# sorts the list of timestamp
	lst_of_TS.sort()
	return lst_of_TS


# Running script 
reaction_id= input("What is the reaction ID?") # by default, user input is a string

path = str('/Users/nicolekim/Dropbox/' + reaction_id)
# obtain the current working directory 
dirpath = os.getcwd()
# print the current working directory so that we can check later if we've changed the directory. 
print("Current working directory %s" % dirpath)

# change the current working directory to the path in DropBox
os.chdir(path)
# Check current working directory.
dirpath = os.getcwd()

print("Directory changed successfully %s" % dirpath)
# create a csv file with the following name structure 
csvname = str('summary_' +  reaction_id + ".csv")
csvpath = os.path.join(dirpath, csvname)

lst_current_indices = [0]
# intitiate two variables: one for means of R, G, and B, and variances of R, G, and B 
means = []
variances = []


i = 0
while i==0:
	# dashboard() - initialize dashboard
	lst_of_TS = getdropbox()
# obtain the last image file 
	last_img_index = lst_current_indices[-1]
#  download the image. 
	image_array = np.load(str(lst_of_TS[last_img_index])+ '.npy') # numpy array for image data
# open the csv file 
	csvfile = open(csvpath, 'r')
	reader = csv.reader(csvfile)
# use the list function to convert the iterable (tuple, string, set, dictionary) in the reader to a list.
	my_csv_data = list(reader)
# go to the correct line in the csv file determined by the index previously obtained.  
	rawdata = my_csv_data[last_img_index]
	csvfile.close()
# sokit the raw data 
	data = rawdata #rawdata.split(',')
	mean_array = [float(data[1]), float(data[2]), float(data[3])] # array of mean RGB values
	var_array = [float(data[4]), float(data[5]), float(data[6])]  # array of variance of RGB values
	# make the arrays to give to Data Analysis Team
	means.append(mean_array)
	variances.append(var_array)

	means_temp = np.array(means)
	variances_temp = np.array(variances)
# run the dasbord function using the parameters obtained from the correct line in the csv file and the the image array of the raw image. 
	dashboard(means_temp, variances_temp, image_array)

	# increment index by 1 
	lst_current_indices.append(last_img_index+1)


	# Data analysis plot function(output) updates the dashboard
	time.sleep(0.5)

	#exit()
