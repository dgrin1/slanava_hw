import numpy as np
T = int(input("Enter the period of the orbit in seconds "))

G = 6.67*10**-11 #m**3*kg**-1*s**-2
M = 5.97*10**24 #kg
R = 6.371*10**6 #m

h = ((G*M*T**2)/(4*np.pi**2))**(1/3) - R

print("For the given period, the altitude in meters is ", h)
