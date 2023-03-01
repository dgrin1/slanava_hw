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

def J_rec(m,x): #J_rec = J calculated through recursion
	if m == 0:
		return J(0,x) #utilize original function J(m,x) to calculate J0 and J1
	if m == 1:
		return J(1,x)
	else:
		return (2*m/x)*J_rec(m-1,x)-J_rec(m-2,x)

x = np.linspace(1,20) #x values

# print(J(2,x)) #testing to make sure it works
# print(J(3,x))
# print(J(4,x))
# print(J_rec(2,x))
# print(J_rec(3,x))
# print(J_rec(4,x))

J2 = (J_rec(2,x)-J(2,x))/J_rec(2,x) #calculate fractional error for n = 2,3,4
J3 = (J_rec(3,x)-J(3,x))/J_rec(3,x)
J4 = (J_rec(4,x)-J(4,x))/J_rec(4,x)

plt.plot(x,J2,'r')
plt.plot(x,J3,'g')
plt.plot(x,J4,'b')
plt.legend(['n=2','n=3','n=4'])
plt.xlabel('x values')
plt.ylabel('Fractional Error')
plt.title('Fractional Error between Methods of Computing Bessel Functions')
plt.show()