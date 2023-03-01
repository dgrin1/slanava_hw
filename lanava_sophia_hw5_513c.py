#by sophia lanava, gaussian quadrature code provided by Mark Newman
import numpy as np
import matplotlib.pyplot as plt
import math as math
from gaussxw import gaussxwab

n = 5

def hermite(n,x): #define the hermite polynomial
	if n==0:
		return 1
	if n==1:
		return 2*x
	else:
		return 2*x*hermite(n-1,x) - (2*n*hermite(n-2,x))

def wavefunct(n,x): #define the wave function
	return (1/(np.sqrt((2**n)*math.factorial(n)*np.sqrt(np.pi)))) * np.exp(-x**2/2) * hermite(n,x)

def f(x): #define the function being integrated
	return x**2*(abs(wavefunct(n,x)))**2

N = 100 #number of points
a = -10 #limits
b = 10

x,w = gaussxwab(N,a,b) #use gaussian quadrature
s = 0.0
for k in range(N):
	s += w[k]*f(x[k])

solution = np.sqrt(s) #take the square root
print(solution)

