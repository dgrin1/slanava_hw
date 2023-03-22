#by sophia lanava
from numpy import array,arange
import matplotlib.pyplot as plt

sigma = 10 #define constants
r_ = 28
b_ = 8/3

def f(r,t):
	x = r[0]
	y = r[1]
	z = r[2]
	fx = sigma*(y-x) #input equations
	fy = r_*x-y-x*z
	fz = x*y-b_*z
	return array([fx,fy,fz],float)

a = 0.0 #boundaries
b = 50
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = array([0,1,0],float) #runge kutta 4th order integration
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])				
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,ypoints)
plt.title('Lorenz Equations: Y vs Time')
plt.xlabel('Time')
plt.ylabel('y')
plt.show()