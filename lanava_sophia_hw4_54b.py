#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt

def f(m,x,t): #define the bessel function
	return np.cos(m*t-x*np.sin(t))

N = 100 #set the number of points

def J(m,x): #calculate the value of Jm(x)
	a = 0
	b = np.pi
	h = (b-a)/N
	Sum = f(m,x,a)+f(m,x,b) #Simpson's rule
	for i in range(1,N): 
		t = a+i*h
		if i%2==1: #even
			Sum += 4*f(m,x,t)
		else: #odd
			Sum += 2*f(m,x,t)
	return Sum*(h/3)*(1/np.pi)

def I(lmbda,r): #intensity function
	k = 2*np.pi/lmbda
	return ((J(1,k*r))/(k*r))**2

wavelength = 0.5 #micrometers
points = 500
separation = 0.01

intensity = np.empty([points,points],float) 

for i in range(points):
    y = separation*(i-points/2)
    for j in range(points):
        x = separation*(j-points/2)
        r = np.sqrt((x)**2+(y)**2)
        if r < 0.00001: #limit as r approaches 0
        	intensity[i,j] = 0.5
        else:
        	intensity[i,j] = I(wavelength,r)

plt.imshow(intensity,vmax=0.01,cmap='hot',extent=(-500,500,-500,500))
plt.title('Diffraction Pattern of a Telescope')
plt.gray()
plt.show()