import numpy as np

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

Z = int(input("Enter the atomic number ")) #input is 28
listB = []
listA = []
listBA = []

for A in range(Z,3*Z+1): #all values of A in between Z and 3Z
    listA.append(A)
    if A%2!=0: #if A is odd
        a5 = 0.0
    elif A%2==0 and Z%2==0: #if A and Z are even
        a5 = 12.0
    else: #all other scenarios
        a5 = -12.0

    B = a1*A - a2*(A**(2./3.)) - a3*((Z**2.)/(A**(1./3.))) - a4*(((A-2.*Z)**2.)/A) + a5/(A**(1./2.)) #calculate the value of B
    BA = B/A #calculate the binding energy per nucleon, the total binding energy divided by the number of nuclei
    listB.append(B)
    listBA.append(B/A)
    most_stable = listA[listBA.index(max(listBA))] #the most stable atomic mass number
    per_nuc = listBA.index(max(listBA))/most_stable #the binding energy per nucleon of the most stable atomic mass number

print("The most stable nucleus is ", most_stable) #returns 58
print("The binding energy per nucleon is ", per_nuc) #returns 0.517
