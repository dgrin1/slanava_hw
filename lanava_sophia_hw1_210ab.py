A = int(input("Enter the atomic mass number ")) #input is 58
Z = int(input("Enter the atomic number ")) #input is 28

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

def a5det(A,Z): #det = determine
    if A%2!=0:
        return 0.0
    elif A%2==0 and Z%2==0:
        return 12.0
    else:
        return -12.0

def Bdet(A,Z,a5):
    return a1*A - a2*(A**(2./3.)) - a3*((Z**2.)/(A**(1./3.))) - a4*(((A-2.*Z)**2.)/A) + a5/(A**(1./2.))

a5 = a5det(A,Z)
B = Bdet(A,Z,a5)
print("The binding energy is ", B) #receive a value of 493.936
print("The binding energy per nucleon is ", B/A) #receive a value of 8.516
