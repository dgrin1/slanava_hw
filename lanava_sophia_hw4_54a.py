#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt

def f(m,x,t): #define the bessel function
	return np.cos(m*t-x*np.sin(t))

N = 1000 #set the number of points

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

x = np.linspace(0,20)
y1 = J(0,x)
y2 = J(1,x)
y3 = J(2,x)

plt.plot(x,y1,'r')
plt.plot(x,y2,'g')
plt.plot(x,y3,'b')
plt.legend(['J0','J1','J2'])
plt.title('Bessel Functions')
plt.show()
