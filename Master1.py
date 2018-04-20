import os
import glob
import numpy as np
import time

from checkdropbox import checkdropbox

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

# The timestamp of the last image detected by the Master script (type = integer)
last_image = 20180410175529 # test sample, FIX THIS BEFORE RUNNING

i = 0
while i=0:
	flag, output = checkdropbox()
	if flag = True:
		# Data Analysis function(output)
	time.sleep(3)




