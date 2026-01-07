# Write a program to find sum of n numbers using recursion
def sum(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum(n-1)
    
n=int(input("Enter the value of n"))
result=sum(n)
print(result)