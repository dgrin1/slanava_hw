#by sophia lanava
from math import sin, cos
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

plt.rc('text',usetex=True) #use LaTeX

g = 9.81 #acceleration due to gravity, m/s
l = 0.1 #length of the pendulum string in meters
C = 2 #s^-1
O = 10 #s^-1
theta_0 = 0 #angle at which pendulum was initially released, degrees
omega_0 = 0

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = (-g/l)*sin(theta)+C*cos(theta)*sin(O*t)
    return array([ftheta,fomega],float)

a = 0.0 #limits
b = 100
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
theta_points = []
omega_points = []

r = array([theta_0,omega_0],float) #runge-kutta 4th order integration
for t in tpoints:
    theta_points.append(r[0])
    omega_points.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,theta_points)

#plt.plot(theta_points,omega_points)

plt.title('Angle of Displacement of a Driven Pendulum Over Time')
plt.xlim(0,100)
plt.xlabel('Time')
plt.ylabel('Angle')
plt.show()