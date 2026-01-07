# Write a program to find sum of following series using recursive function:
# 1!+2!+3!+4!.....+n!
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
    
def sum(n):
    if n==1:
        return 1
    else:
        return fact(n)+sum(n-1)
        
n=int(input("Enter value of n"))
result=sum(n)
print(result)
   
    

