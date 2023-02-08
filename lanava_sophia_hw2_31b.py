#by Sophia Lanava, sunspots.txt data provided by Mark Newman
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt,array,dot,sqrt,sin,cos,linspace,log

plt.ion()
data=loadtxt("sunspots.txt",float)

x=data[:,0]
y=data[:,1]

n=1000 
plt.plot(x,y,'ro',markersize=3)

plt.xlim([0,n]) #limit the number of datapoints along the x axis to 1000 (n=1000, defined above)
plt.xlabel("Time in months since January 1749")
plt.ylabel("Number of Sunspots")
plt.title("Number of Sunspots as a Function of Time")

