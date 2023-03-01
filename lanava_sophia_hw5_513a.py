#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt
import math as math

def hermite(n,x): #define the hermite polynomial
	if n == 0:
		return 1
	if n == 1:
		return 2*x
	else:
		return (2*x*hermite(n-1,x)) - (2*n*hermite(n-2,x))

def wavefunct(n,x): #define the wave function
	return (1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))) * np.e**(-x**2/2) * hermite(n,x)

x_values = np.linspace(-4,4,100) #evaluate in the range x = -4 to x = 4
y_values = []

for n in range(4): 
	y_val = []
	for x in x_values:
		ans = wavefunct(n,x)
		y_val.append(ans)
	y_values.append(y_val)

plt.plot(x_values,y_values[0]) #plot
plt.plot(x_values,y_values[1])
plt.plot(x_values,y_values[2])
plt.plot(x_values,y_values[3])
plt.legend(['n=0','n=1','n=2','n=3'])
plt.xlabel('x values')
plt.title('Harmonic Oscillator Wave Functions for n = 0,1,2,3')
plt.show()