#by Sophia Lanava
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt,array,dot,sqrt,sin,cos,linspace,log,pi

plt.rc('text',usetex=True) #use LaTeX

theta=linspace(0,2*pi) #theta is the range of values between o and 2pi

x=2*cos(theta)+cos(2*theta) #calculate x and y for each value of theta
y=2*sin(theta)-sin(2*theta)

plt.plot(x,y)
plt.xlabel(r"$2cos(\theta) + cos(2\theta)$") #use LaTeX formatting in labels so theta appears as the actual greek letter
plt.ylabel(r"$2sin(\theta) - sin(2\theta)$")
plt.title("Deltoid Curve")
plt.show()