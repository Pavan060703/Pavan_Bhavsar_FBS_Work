n=int(input("Enter the number till you want all integers not divisible by 2 and 3"))
for i in range(1,n+1):
    if i%2!=0 and i%3!=0:
        print(i)