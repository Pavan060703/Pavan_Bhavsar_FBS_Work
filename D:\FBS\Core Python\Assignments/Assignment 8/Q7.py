def sum_digits(num):
    sum=0
    digit=0
    for i in range(1,num+1):
        digit=num%10
        sum=sum+digit
        num=num//10
    
    return sum
n=int(input("Enter the number"))
print(sum_digits(n))