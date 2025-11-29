# Write a program to check if given number is Armstrong or not using recursive function.
def count_digits(n):
    if n==0:
        return 0
    else:
        return 1+count_digits(n//10)
    
def arm_Strong(n,power):
    if n==0:
        return 0
    return (n%10) ** power + arm_Strong(n//10,power)

n=int(input("Enter a number"))
digits=count_digits(n)
result=arm_Strong(n,digits)
if result==n:
    print(n,"is an armstrong number")
else:
    print(n, "is not a armstrong number")