#by sophia lanava
import numpy as np

# Constants
M = 9.1094e-31     #mass of electron, kg
hbar = 1.0546e-34  #planck's constant over 2*pi, J*s
e = 1.6022e-19     #electron charge, C
L = 5.0e-10        #well width, m
a = 10             #a value, eV 
# N = 10
# H = np.zeros((N,N))

m = int(input("Enter a value for m "))
n = int(input("Enter a value for n "))

def Hmn(m,n):
	if m == n:
		return (np.pi*hbar*n)**2/(2*M*L**2)*e+a/2
	elif (m+n)%2 == 1:
		return -8*a/(np.pi**2)*m*n/(m**2-n**2)**2
	else:
		return 0

ans = Hmn(m,n)
print(ans)