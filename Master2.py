import os
import glob
import numpy as np
import csv

import sys
sys.path.append('/Users/nicolekim/Desktop/PS50/repo/DataAnalysis')
from dashboard_function import dashboard # Data Analysis dashboard plot function

import time

def getdropbox():
	"""Checks dropbox and updates list of timestamps as integers.
	Note: Assumes we're inside the dropbox directory.

	Returns:
	========
	lst_of_TS : list of timestamps (as integers not filenames)
	"""
	lst_of_TS = []

	for file in glob.glob("*.npy"):

		#print(file)
		name = file.split('.') # file is the name of the file as a list of 2 string elements
		timestamp_str = name[0] # grab the timestamp portion of the file name
		timestamp_int = int(timestamp_str) # convert the timestamp into an integer
		lst_of_TS.append(timestamp_int)

	lst_of_TS.sort()
	return lst_of_TS


## Running script 
reaction_id= input("What is the reaction ID?") # by default, user input is a string

path = str('/Users/nicolekim/Dropbox/' + reaction_id)

dirpath = os.getcwd()
print("Current working directory %s" % dirpath)

os.chdir(path)
# Check current working directory.
dirpath = os.getcwd()

print("Directory changed successfully %s" % dirpath)

csvname = str('summary_' +  reaction_id + ".csv")
csvpath = os.path.join(dirpath, csvname)
lst_current_indices = [0]
means = []
variances = []


i = 0
while i==0:
	# dashboard() - initialize dashboard
	lst_of_TS = getdropbox()
	
	last_img_index = lst_current_indices[-1]
	image_array = np.load(str(lst_of_TS[last_img_index])+ '.npy') # numpy array for image data

	csvfile = open(csvpath, 'r')
	reader = csv.reader(csvfile)
	my_csv_data = list(reader)
	rawdata = my_csv_data[last_img_index]
	csvfile.close()

	data = rawdata #rawdata.split(',')
	mean_array = [float(data[1]), float(data[2]), float(data[3])] # array of mean RGB values
	var_array = [float(data[4]), float(data[5]), float(data[6])]  # array of variance of RGB values
	# make the arrays to give to Data Analysis Team
	means.append(mean_array)
	variances.append(var_array)

	means_temp = np.array(means)
	variances_temp = np.array(variances)

	dashboard(means_temp, variances_temp, image_array)

	# increment index by 1 
	lst_current_indices.append(last_img_index+1)


	# Data analysis plot function(output) updates the dashboard
	time.sleep(0.5)

	#exit()
