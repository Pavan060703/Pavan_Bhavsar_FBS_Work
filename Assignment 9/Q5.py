# Write a program to find factorial using recursion
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter value of n:"))
result=fact(n)
print(f"The factorial of {n} is ",result)