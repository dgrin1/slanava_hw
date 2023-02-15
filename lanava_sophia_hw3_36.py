#by sophia lanava
import numpy as np
import matplotlib.pyplot as plt


def logis(r, x0, N):    
    x=x0
    x_list=[x0]
    for i in range (N-1):      
        x=r*x*(1-x)
        x_list.append(x)

r_list=np.linspace(1,4,300) #list of r values
x0=0.5 #x=1/2
N=2000 #2000 iterations, only the second 1000 will be plotted, the first 1000 are to account for any limits or convergences

def logistic(r):
    x_list=[x0]    
    for i in range (N-1):
        x_list.append(r*x_list[-1]*(1-x_list[-1]))
    return x_list[1000:] #return only the iterations from 1000 onward

x_values=[] #create arrays of the values
r_values=[]
for r in r_list:
    x_values.append(logistic(r))
    r_values.append(r) 

x_values=np.array(x_values)
r_values=np.array(r_values)

plt.xlabel("The value of r")
plt.ylabel("The value of x")
plt.title("The Feigenbaum Plot")
plt.plot(r_values, x_values, 'ko', markersize=0.05)
plt.show()