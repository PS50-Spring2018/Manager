import os
import glob
import numpy as np

def checkdropbox(dirpath,csvpath,last_image):

	# The timestamp of the last image detected by the Master script (type = integer)
	# last_image = 20180410175529 # test sample, FIX THIS BEFORE RUNNING

	for file in glob.glob("*.npy"):
		name = file.split('_') # file is the name of the file as a list of 2 string elements
		timestamp_str = name[0] # grab the timestamp portion of the file name
		timestamp_int = int(timestamp_str) # convert the timestamp into an integer
		if timestamp_int > last_image: # is file is more recent than the last image detected by Master script? (both variables are type = int)
			# download .npy file
			image_path = os.path.join(dirpath, file) # path to image file
			image_array = np.load(image_path) # contains the np array of image
			# redownload the csv of means and variances
			mastercsv = open(csvpath, 'r')
			templist = []
			for line in mastercsv:
				templist.append(line)
			data = templist[-1].split(',') # grab the last line of the csv, split into constitute parts
			mean_array = np.array([float(data[1]), float(data[2]), float(data[3])]) # array of mean RGB values
			var_array = np.array([float(data[4]), float(data[5]), float(data[6])]) # array of variance of RGB values
			# make the array to give to Data Analysis Team
			fulldata = []
			fulldata.append(mean_array)
			fulldata.append(var_array)
			fulldata.append(image_array)
			fulldata_array = np.array(fulldata) # the input for the Data Analysis Team's functions

			# reset last_image value to the last image worked with
			# UNCOMMENT THIS WHEN READY TO TEST MORE THAN 1 IMAGE: 
			last_image = timestamp_int

			mastercsv.close()

			return True, fulldata_array, last_image

		else:
			return False, None, None
		