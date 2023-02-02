import numpy as np

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

listB = []
listA = []
listBA = []

for Z in range(1,101): #all values of Z in between 1 and 100
    for A in range(Z,3*Z+1): #all values of A in between Z and 3Z
        listA.append(A)
        if A%2!=0: #if A is odd
            a5 = 0.0
        elif A%2==0 and Z%2==0: #if A and Z are even
            a5 = 12.0
        else: #any other scenarios
            a5 = -12.0
        B = a1*A - a2*(A**(2./3.)) - a3*((Z**2.)/(A**(1./3.))) - a4*(((A-2.*Z)**2.)/A) + a5/(A**(1./2.)) #determine the value of B
        BA = B/A #determine the binding energy per nucleon, the total binding energy divided by the number of nuclei
        listB.append(B)
        listBA.append(B/A)
        most_stable = listA[listBA.index(max(listBA))]

print("The most stable nucleus is ", most_stable, "at atomic number ", Z)
#I am going to be completely honest, I worked on this problem for upwards of 3 hours, and I just couldn't figure out this last part
