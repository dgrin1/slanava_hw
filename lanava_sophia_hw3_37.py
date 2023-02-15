#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_comp(max_iter,num,nx,ny): #max_iter is the number of iterations, |z| cannot exceed num
	x=np.linspace(-2,2,nx) #nx and ny specify the number of points
	y=np.linspace(-2,2,ny)
	c=x[:,np.newaxis]+1j*y[np.newaxis,:] #I am unsure if we have learned np.newaxis, it makes it so that another dimension is added to the array
	z=c
	for i in range(max_iter):
		z=z**2+c
	mandelbrot_set=(abs(z)<num) #the mandelbrot set is the set where the absolute value of z hasn't exceeded num (2 in this case)
	return mandelbrot_set

mandelbrot_set=mandelbrot_comp(1000,2,1000,1000) #number of iterations, value |z| cannot exceed, number of points along x and y

plt.imshow(mandelbrot_set.T, extent=[-2,2,-2,2]) 
plt.gray()
plt.xlabel("The real part of c")
plt.ylabel("The imaginary part of c")
plt.title("The Mandelbrot Fractal")
plt.show()

