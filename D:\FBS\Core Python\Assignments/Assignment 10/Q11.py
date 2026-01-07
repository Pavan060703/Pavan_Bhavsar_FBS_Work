#Write a program to print all numbers which are divisible by m and n in the list.
def divisible(li,m,n):
    new_list=[]
    for i in li:
        if i%m==0 and i%n==0:
            new_list.append(i)
    return new_list

li=[10,20,30,40,50,60,70]
m=int(input("Enter the value of m"))
n=int(input("Enter the value of n"))
result=divisible(li,m,n)
print(result)