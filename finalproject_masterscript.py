# import libraries needed
import numpy as np 
import scipy as sp
import seaborn as sb 
import matplotlib.pyplot as plt
import csv 

#ask for user input of how often to take images, how many total images
rate = int(input('How often (in images/minute) should an image be captured?'))
total = int(input('How many images would you like to capture in total?'))

#pass those numbers as input to group 1 function to initialize camera/collect image/save to dropbox
	# first import the function
from group1filename import whatevertheycallthefxn
	#what inputs does that function take?
	#output = a file saved to dropbox, yes?

#detect when there’s a new file in dropbox
	#function saved in another file, Nicole is writing

#pull data from dropbox
	#function saved in another file, Nicole is writing


#create object (of class image) for each image file
	#how to name the object?

# append image object to an experiment object, which is a list of images
	#so we need to make an experiment class as well - are we still doing this?

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
