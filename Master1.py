import os
import glob
import numpy as np
import time

from checkdropbox import checkdropbox # dropbox function, check for new images, if new, download relevant info
from dashboard_function import dashboard # Data Analysis dashboard plot function

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

##Function: Check dropbox for new image files and if yes, download new images files and redownload CSV

last_image = 20180410175529

i = 0
while i==0:
	# dashboard() - initialize dashboard
	flag, output, last_image = checkdropbox(dirpath, csvpath,last_image)
	print(output)
	# if flag == True:
		# Data analysis plot function(output) updates the dashboard
	time.sleep(3)

	exit()




