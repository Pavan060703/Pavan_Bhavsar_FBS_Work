# Write a program to check whether a number is prime or not using recursion
def isPrime(n,j=2):
    if n<=1:
        return False
    if j*j>n:
        return True
    if n%j==0:
        return False
    return isPrime(n,j+1)

n=int(input("Enter the number"))
if isPrime(n):
    print(n,"is a prime number")
else:
    print(n," is not a prime number")