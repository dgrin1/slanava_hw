import numpy as np

M = 1.9891e30 #kg, mass of sun
G = 6.6738e-11 #m**3kg**-1s**-2

l1 = float(input("Enter length of perihelion "))
v1 = float(input("Enter velocity at perihelion "))

v2 = (2*G*M/l1*v1) - v1 #velocity at aphelion
l2 = (l1*v1)/v2 #length of aphelion
a = (l1+l2)/2 #semi-major axis
b = np.sqrt(l1*l2) #semi-minor axis
T = (2*np.pi*a*b)/(l1*v1) #orbital period
e = (l2-l1)/(l2+l1) #eccentricity

print("The length of the aphelion is ", l2)
print("The velocity at the aphelion is ", v2)
print("The orbital period is ", T)
print("The eccentricity is ", e)
