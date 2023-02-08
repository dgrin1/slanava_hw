#by Sophia Lanava, sunspots.txt data provided by Mark Newman
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt,array,dot,sqrt,sin,cos,linspace,log

plt.ion()
data=loadtxt("sunspots.txt",float)

x=data[:,0]
y=data[:,1]

n=1000

plt.xlim([0,n])
plt.xlabel("Time in months since January 1749")
plt.ylabel("Number of Sunspots")
plt.title("Number of Sunspots as a Function of Time")

r=5
avg=[]
for a in range(r,len(data[:,0])-r): #define the range of values for which the average should be calculated
	avg.append((1/(2*r+1)*sum(data[a-r:a+r,1]))) #calculate the running average
	
plt.plot(x,y,'ro',markersize=3) #plots the original data
plt.plot(avg,'b') #plots the running average, in a different color 
plt.show()