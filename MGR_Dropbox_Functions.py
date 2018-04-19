# Script for Dropbox functions: 
	# (1) Check dropbox for new image files 
	# (2) Download new image files and redownload CSV of relevant image information



# Use module os, use Terminal, use cd to change to (or input: what is the path to the dropbox)

# Change working directory to Dropbox

import os

path = '/Users/nicolekim/Dropbox'

dirval = os.getcwd()
print("Current working directory %s" % dirval)

os.chdir(path)
# Check current working directory.
dirval = os.getcwd()

print("Directory changed successfully %s" % dirsval)



# Function: Check dropbox for new image files and if yes, download new images files and redownload CSV
# Webcam interface filename convention: eg 20180410175530 = year, month, date, hour (24 hour), minute, seconds
last_im = ' '

if 


# Save to csv file - each row represents a different image and columns contain info on that image
# Update csv file in real time

