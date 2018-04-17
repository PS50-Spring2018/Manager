# import libraries needed
import numpy as np 
import scipy as sp
import seaborn as sns 
import matplotlib.pyplot as plt
import csv 

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

#pass those numbers as input to group 1 function to initialize camera/collect image/save to dropbox
	# first import the function
from group1filename import whatevertheycallthefxn
	#what inputs does that function take?
	#output = a file saved to dropbox, yes?

#detect when there’s a new file in dropbox
	#function saved in another file, Nicole is writing

#pull data from dropbox
	#function saved in another file, Nicole is writing
from nicolefilename import droboxdatafxn

#create object (of class image) for each image file
	#first import the class - currently called "constructor", may want to rename for clarity
from constructor import Image
	#how to name the object? same as file?
imagename = Image(inputs)

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
