import numpy as np

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

listB = []
listA = []
listBA = []

for Z in range(1,100):
    for A in range(Z,3*Z+1):
        listA.append(A)
        if A%2!=0:
            a5 = 0.0
        elif A%2==0 and Z%2==0:
            a5 = 12.0
        else:
            a5 = -12.0
        B = a1*A - a2*(A**(2./3.)) - a3*((Z**2.)/(A**(1./3.))) - a4*(((A-2.*Z)**2.)/A) + a5/(A**(1./2.))
        BA = B/A
        listB.append(B)
        listBA.append(B/A)
        most_stable = listA[listBA.index(max(listBA))]

print("The most stable nucleus is ", most_stable, "at atomic number ", Z)
