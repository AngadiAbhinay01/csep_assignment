#Python program to find the factorial of a given number

n=int(input("Enter the number:"))
def factorial(n):
	if (n==0 or n==1):
		return 1
	else:
		return n*factorial(n-1)
res=factorial(n)
print(res)
