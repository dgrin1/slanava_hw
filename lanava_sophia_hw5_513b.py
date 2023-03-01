#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt
import math as math

def hermite(n,x): #define the hermite polynomial
	if n==0:
		return 1
	if n==1:
		return 2*x
	else:
		return (2*x*hermite(n-1,x)) - (2*n*hermite(n-2,x))

def wavefunct(n,x): #define the wave function
	return (1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))) * np.e**(-x**2/2) * hermite(n,x)

n = 30 #only a single value of n
x_values = np.linspace(-10,10,100) #evaluate over the range of x = -10 to x = 10
y_values = []

for x in x_values:
	ans = wavefunct(n,x)
	y_values.append(ans)

plt.plot(x_values,y_values) #plot
plt.xlabel('x values')
plt.title('Harmonic Oscillator Wave Functions for n = 30')
plt.show()