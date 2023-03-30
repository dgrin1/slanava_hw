#by sophia lanava
from math import sin, cos
from numpy import array,arange
import numpy as np
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

plt.rc('text',usetex=True) #use LaTeX

g = 9.81 #acceleration due to gravity, m/s
l = 0.4 #length of the pendulum string in meters
m = 1
theta1_0 = np.pi/2 #angle at which pendulum was initially released, degrees
theta2_0 = np.pi/2
omega1_0 = 0
omega2_0 = 0

def f(r,t):
	theta1 = r[0]
	theta2 = r[1]
	omega1 = r[2]
	omega2 = r[3]
	ftheta1 = omega1
	ftheta2 = omega2
	fomega1 = -(omega1**2*sin(2*theta1 - 2*theta2) + 2*omega2**2*sin(theta1 - theta2) + (g/l)*(sin(theta1 - 2*theta2) + 3*sin(theta1)))/(3 - cos(2*theta1 - 2*theta2))
	fomega2 = (4*omega1**2*sin(theta1 - theta2) + omega2**2*sin(2*theta1 - 2*theta2) + 2*(g/l)*(sin(2*theta1 - theta2) - sin(theta2)))/(3 - cos(2*theta1 - 2*theta2))
	return array([ftheta1, ftheta2, fomega1, fomega2],float)

a = 0.0 #limits
b = 100.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
theta1_points = []
theta2_points = []
omega1_points = []
omega2_points = []
E_points = np.zeros(1000)

r = array([theta1_0,theta2_0,omega1_0,omega2_0],float) #runge-kutta 4th order integration
for t in tpoints:
    theta1_points.append(r[0])
    theta2_points.append(r[1])
    omega1_points.append(r[2])
    omega2_points.append(r[3])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

theta1_points = np.array(theta1_points) #turn lists into arrays
theta2_points = np.array(theta2_points)
omega1_points = np.array(omega1_points)
omega2_points = np.array(omega2_points)

for t in tpoints: #this took me so so so long to get working
	E = (m*l**2*(np.power(omega1_points,2)) + (1/2)*np.power(omega2_points,2) + np.multiply(omega1_points,omega2_points)*np.cos(np.subtract(theta1_points,theta2_points)) - m*g*l*(2*np.cos(theta1_points) + np.cos(theta2_points)))
	np.append(E_points,E)

E_points = np.array(E_points)

#print(E_points)
plt.plot(tpoints,E_points)

#plt.plot(theta_points,omega_points)

plt.title('Double Pendulum')
plt.xlabel('Time')
plt.ylabel('Energy')
plt.show()