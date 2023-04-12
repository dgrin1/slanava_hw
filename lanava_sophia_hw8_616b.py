#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt

#constants
G = 6.674e-11    #grav constant, m**3 kg**-1 s**-2
M = 5.974e24     #Earth mass, kg
m = 7.348e22     #Moon mass, kg
R = 3.844e8      #distance between Earth and Moon, m
w = 2.662e-6     #angular velocity, s**-1

def f(r):
	return (G*M/r**2) - (G*m/(R-r)**2) - (w**2*r)

def secant(): #secant method
	#pick starting values of r in between 0 and R
	r1 = 3.0e4
	r2 = 3.0e6
	for x in range(20): #find a range that doesn't return an error of dividing by 0
		r = r2-f(r2)*(r2-r1)/(f(r2)-f(r1))
		r1 = r2
		r2 = r
	return r

dist = secant()
print('The distance between Earth and L1 is', dist)