# import libraries needed for project
import numpy as np 
import scipy as sp
import seaborn as sns 
import matplotlib.pyplot as plt
import time
import csv 
import cv2
import os
import glob


#Important note: Sublime text doesn't support user input so below are instructions that install some packages that allow for user input function
# in Sublime press ctrl + shift + P (linux command in ST for 'goto anything').
# Type in 'install',
# click on 'sublime package control: install package'.
# Then select SublimeREPL. It will install it automatically.
# To use it go to Tools>sublimerepl>python>python-RUNcurrentfile - this will run the script in a new tab, but with user input

#ask for user input of how often to take images, how many total images
rate = input('How often (in images/minute) should an image be captured?')
print(rate)
total_images = input('How many images would you like to capture in total?')
print(total_images)

#import Dropbox functions
from MGR_Dropbox_functions import filecheck
from constructorfunctions import getImageraw, getImagecontourdata
#import camera controls
from CameraOps import stream, snap

#pass user input to group 1 function to initialize camera/collect image/save to dropbox
stream()
for i in range(0,total_images):
	#take image
	snap()		#output of this function is a file saved to dropbox, yes?

	#go ahead and download this from dropbox
	filecheck()
	getImageraw()			#where does this save to? need to know in order to implement Image class
	getImagecontourdata()	#same question as above

	#wait the appropriate amount of time before taking the next image
	time.sleep(60/rate)

	#repeat!

#Import image class - file currently called "constructor", may want to rename for clarity
from constructor import Image
#next import functions
from constructorfunctions import *

#create an Image object for each image file downloaded from Dropbox
imagelist = []
for file in whateverfolderitis: 		#FIX this
	#open file
	f = open(filename,'r')

	#read whatever line it is that has the values we want: FIX THIS
	line = f.readline() 

	#read necessary components of file to get inputs for image class: FIX THIS
	red = 
	green = 
	blue = 
	meanred = getmeanRed()
	meangreen = getmeanGreen()
	meanblue = getmeanBlue()
	variancered = getvarianceRed()
	variancegreen = getvarianceGreen()
	varianceblue = getvarianceBlue()

	#create instance of Image
	uniqueimagenamesomehow = Image(red, green, blue, meanred, meangreen, meanblue, variancered, variancegreen, varianceblue)
	#close file
	f.close()
	# append image object to list of images
	imagelist.append(uniqueimagenamesomehow)

#pool images into an experiment object: this will have the inputs for the analysis function as attributes
from experimentclass import Experiment 
experimentnamesomehowwhatdowewanttocallthis = Experiment(imagelist)



#call group 3 analysis functions on experiment object - what inputs are they using specifically/what's their syntax?
	#first import their function
from PS50DataAnalysis import *
	#a - graph of R, G, B vs. iteration (?)
	#b - actual image
	#c - avg RGB path, mapped onto color wheel
	#d - avg color at each time step

#check if dropbox is full - where should this go? Particularly w/ updating in real time, want to make sure that this doesn’t become an issue...
	#call size attribute for each object
	#look at total sum of all of those?

