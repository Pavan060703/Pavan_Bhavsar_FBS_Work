num=int(input("Enter the number of which you want factorial"))
fact=1
if(num==0):
    print("0")
else:
    for i in range(1,num+1):
        fact=fact*i

print(fact)