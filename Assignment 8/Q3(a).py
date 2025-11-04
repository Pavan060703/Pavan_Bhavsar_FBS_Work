#Write a program to find sum of following series using functions
#a.1+2+3+4+.....n
def sum_series(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i

    return sum    

n=int(input("Enter the number"))
print(sum_series(n))
    
