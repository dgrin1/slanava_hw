#by Sophia Lanava
#altered from heat.py by Mark Newman

import numpy as np
import matplotlib.pyplot as plt

A = float(input("Input the average surface temperature "))
B = 12        # Degrees Celsius
tau = 365     # Days
D = 0.1       # m^2/day

def T0(t):  # Calculates the variation in the mean surface temperature at a given point on Earth's surface
	return A+B*np.sin((2*np.pi*t)/tau)

# Constants
L = 20        # Depth in meters
D = 0.1       # Thermal diffusivity, m^2/day
N = 100       # Number of divisions in grid
a = L/N       # Grid spacing
h = 1e-4      # Time-step

T = np.zeros(N+1,float)
T[1:N] = 10   # set value at limits to 10

def iterate(T,tmin,tmax):  # Define a function to conduct the FTCS method of partial differential equation solving
	t = tmin
	c = h*D/a**2
	while t < tmax:
		T[0] = T0(t)
		T[N] = 11
		T[1:N] = T[1:N]+c*(T[2:N+1]+T[0:N-1]-2*T[1:N])
		t += h
	return T

T9 = iterate(T,0,365*9)  # Calculate the temperatures for the first 9 years of the simulation

T10 = T9  # Set the initial temperatures for the 10th year equal to those of the 9th
tmin = 365*9

for tmax in [365*9 + i*(365//4) for i in range(4)]:  # Divide the 10th year into fourths
 	T10 = iterate(T10,tmin,tmax)  # Calculate temperatures for the 10th year of the simulation
 	plt.plot(T10)  #Plot
 	tmin = tmax  # Repeat

plt.legend(['Spring','Summer','Fall','Winter'])  # Label each of the profiles with its corresponding season
plt.xlabel('Depth (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature Profile of Earths Crust - ')
plt.show()