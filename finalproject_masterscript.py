# import libraries needed
import numpy as np 
import scipy as sp
import seaborn as sns 
import matplotlib.pyplot as plt
import time
import csv 
import cv2

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
from constructorfunctions import getImageraw, getImagecontourdata
#import camera controls
from CameraOps import stream, snap

#pass user input to group 1 function to initialize camera/collect image/save to dropbox
stream()
for i in range(0,total_images):
	#take image
	snap()		#output of this function is a file saved to dropbox, yes?

	#go ahead and download this from dropbox
	getImageraw()
	getImagecontourdata()

	#wait the appropriate amount of time before taking the next image
	time.sleep(60/rate)

	#repeat!


#create object (of class image) for each image file
	#first import the class - currently called "constructor", may want to rename for clarity
from constructor import Image
	#next import functions
from constructorfunctions import getmeanRed, getmeanGreen, getmeanBlue
from constructorfunctions import getvarianceRed, getvarianceGreen, getvarianceBlue
	#how to name the object? same as file?
#imagename = Image(inputs)



# append image object to an experiment object, which is a list of images
	#so we need to make an experiment class as well - are we still doing this?
from experimentclassfile import Experiment 
experimentname = Experiment(inputs)



#call group 3 analysis functions on experiment object - what inputs are they using specifically/what's their syntax?
	#first import their function
from group3filename import whateveritis, whatever2, whatever3
	#a - graph of R, G, B vs. iteration (?)
	#b - actual image
	#c - avg RGB path, mapped onto color wheel
	#d - avg color at each time step

#check if dropbox is full - where should this go? Particularly w/ updating in real time, want to make sure that this doesn’t become an issue...
	#call size attribute for each object
	#look at total sum of all of those?

install

