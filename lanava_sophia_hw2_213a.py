#by Sophia Lanava
def catalan(n):
	if n==0:
		return 1.0
	else:
		return ((4*n-2)/(n+1))*catalan(n-1)
n=100 
		
print("The", n, "th Catalan number is", catalan(n))