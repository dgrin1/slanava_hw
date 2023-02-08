#by Sophia Lanava, sunspots.txt data provided by Mark Newman
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt,array,dot,sqrt,sin,cos,linspace,log #not all of these are necessary

plt.ion()
data=loadtxt("sunspots.txt",float) #load the data

x=data[:,0] #define x as the first column of the data, time
y=data[:,1] #define y as the second column of the data, number of sunspots

plt.plot(x,y,'ro',markersize=3) #plot x and y

plt.xlabel("Time in months since January 1749") #label axes and title plot
plt.ylabel("Number of Sunspots")
plt.title("Number of Sunspots as a Function of Time")