#by sophia lanava, gaussxw.py file provided by Mark Newman
from gaussxw import gaussxwab
import numpy as np
import matplotlib.pyplot as plt

V = 1e-6 #m^3
p = 6.022e28 #m^-3
theta = 428 #debye temperature, K
kb = 1.381e-23 #boltzmann constant, m^2 kg s^-2 K^-1
T = np.linspace(5,500,50) 

def f(x):
	return (9*V*p*kb*(T/theta)**3)*(x**4*np.exp(x))/(np.exp(x)-1)**2 #heat capacity equation

N = 50
a = 0 #lower limit
b = theta/T #upper limit

x,w = gaussxwab(N,a,b) #use gaussian quadrature
s = 0.0
for k in range(N):
	s += w[k]*f(x[k])

print(s)

plt.plot(T,s,'r')
plt.title('Heat Capacity')
plt.xlabel('Temperature')
plt.ylabel('Cv')
plt.show()