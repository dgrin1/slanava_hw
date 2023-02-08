#by Sophia Lanava
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt,array,dot,sqrt,sin,cos,linspace,log,pi,exp

plt.rc('text',usetex=True) #use LaTeX

x=[]
y=[]

for theta in linspace(0,24*pi):
	r=(exp(cos(theta))-2*cos(4*theta)+sin(theta/12)**5)
	x.append(r*cos(theta))
	y.append(r*sin(theta))

plt.plot(x,y)
plt.xlabel(r"$rcos(\theta)$") #use LaTeX formatting in labels so theta appears as the actual greek letter
plt.ylabel(r"$rsin(\theta)$")
plt.title("Fey's Function")
plt.show()