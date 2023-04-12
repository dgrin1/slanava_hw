#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt

# Constants
M = 9.1094e-31     #mass of electron, kg
hbar = 6.5821e-16  #planck's constant over 2*pi, eV*s
e = 1.6022e-19     #electron charge, C
L = 5.0e-10        #well width, m
a = 10             #a value, eV 
N = 100
H = np.zeros((N,N), float)

# m = int(input("Enter a value for m "))
# n = int(input("Enter a value for n "))

def Hmn(m,n):
	if m == n:
		return (np.pi*hbar*n)**2/(2*M*L**2)*e+a/2
	elif (m+n)%2 == 1:
		return -8*a/(np.pi**2)*m*n/(m**2-n**2)**2
	else:
		return 0

# ans = Hmn(m,n)
# print(ans)

for x in range(0,10):
	for y in range(0,10):
		H[x,y] = Hmn(x+1,y+1)

_, psi = np.linalg.eigh(H)
# print(energy)

def calc_psi(n,xval):
    wavefunction = sum([psi[n,i]*np.sin(np.pi*(i+1)*xval/L) for i in range(100)])
    return np.sqrt(2./L)*wavefunction

# def wavefunct(n,xval):
# 	return sum([psi[n,z]*np.sin(np.pi*(z+1)*xval/L)])

xvals = np.linspace(0,L,100)
ground = calc_psi(0,xvals)
first = calc_psi(1,xvals)
second = calc_psi(2,xvals)

plt.plot(xvals, ground**2, '-r')
plt.plot(xvals, first**2, '-g')
plt.plot(xvals, second**2, '-b')
plt.legend(['Ground', 'First excited', 'Second excited'])
plt.xlabel('Distance (m)')
plt.ylabel('Probability Density')
plt.title('Probability Density of Wavefunctions as a Function of x')
plt.show()