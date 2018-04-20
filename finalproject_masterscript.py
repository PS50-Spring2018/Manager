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


#import Dropbox functions
from MGR_Dropbox_functions import *			#theoretically these are all incorporated within the next file, but just in case
from meanvariancerawcontourimagesfunctions import *

#import camera controls
from CameraOps import stream, snap

#pass user input to group 1 function to initialize camera/collect image/save to dropbox
stream()
for i in range(0,total_images):
	#take image
	snap()		#output of this function is a file saved to dropbox, yes?

	#wait the appropriate amount of time before taking the next image
	time.sleep(60/rate)

	#repeat!

#Import image class - file currently called "constructor", may want to rename for clarity
from constructor import Image

#download files from dropbox - SHOULD THIS BE IN A FOR LOOP??
getrawImage()			
getImagecontourdata()

#create an Image object for each image file downloaded from Dropbox
imagelist = []
for file in whateverfolderitis: 		#FIX this
	getMeanVariance()

	#read necessary components of file to get inputs for image class: FIX THIS
	red = 
	green = 
	blue = 
	meanred = 
	meangreen = 
	meanblue = 
	variancered = 
	variancegreen = 
	varianceblue = 

	#create instance of Image
	uniqueimagenamesomehow = Image(red, green, blue, meanred, meangreen, meanblue, variancered, variancegreen, varianceblue)

	# append image object to list of images
	imagelist.append(uniqueimagenamesomehow)

#pool images into an experiment object: this will have the inputs for the analysis function as attributes
from experimentclass import Experiment 
experimentname = Experiment(imagelist)



#call group 3 analysis functions on experiment object - what inputs are they using specifically/what's their syntax?
	#first import their function
from PS50DataAnalysis import *
Initialize()
Run(experimentname.inputarray)


#check if dropbox is full - where should this go? Particularly w/ updating in real time, want to make sure that this doesn’t become an issue...
	#call size attribute for each object
	#look at total sum of all of those?

