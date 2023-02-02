A = int(input("Enter the atomic mass number ")) #input is 58
Z = int(input("Enter the atomic number ")) #input is 28

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

def a5det(A,Z): #det = determine, want to determine the value of a5 given the values of A and Z
    if A%2!=0: #if A is odd
        return 0.0
    elif A%2==0 and Z%2==0: #if A and Z are even
        return 12.0
    else: #any other scenarios
        return -12.0

def Bdet(A,Z,a5): #determine the value of B
    return a1*A - a2*(A**(2./3.)) - a3*((Z**2.)/(A**(1./3.))) - a4*(((A-2.*Z)**2.)/A) + a5/(A**(1./2.))

a5 = a5det(A,Z) #a5 = the value determined by the function above
B = Bdet(A,Z,a5) #B = the value determined by the function above
print("The binding energy is ", B) #receive a value of 493.936
print("The binding energy per nucleon is ", B/A) #receive a value of 8.516

#I realize in the next two parts that the a5det and Bdet functions aren't necessary
