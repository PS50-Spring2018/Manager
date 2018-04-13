# import libraries needed
import numpy as np 
import scipy as sp
import seaborn as sb 
import matplotlib.pyplot as plt

#ask for user input of how often to take images, how many total images
rate = int(input('How often (in images/minute) should an image be captured?'))
total = int(input('How many images would you like to capture in total?'))

#pass those numbers as input to group 1 function to initialize camera/collect image/save to dropbox

#detect when there’s a new file in dropbox

#pull data from dropbox - four things, according to group 1 google doc:


#create object (of class image) for each image file

# append image object to an experiment object, which is a list of images

#call group 3 analysis functions on experiment object
	#a - graph of R, G, B vs. iteration (?)
	#b - actual image
	#c - avg RGB path, mapped onto color wheel
	#d - avg color at each time step

#check if dropbox is full - where should this go? Particularly w/ updating in real time, want to make sure that this doesn’t become an issue...
	#call size attribute for each object
	#look at total sum of all of those?
