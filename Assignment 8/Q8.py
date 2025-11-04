def reverse_number(num):
    reverse=0
    digit=0
    while(num>0):
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse

n=int(input("Enter the number"))
print(reverse_number(n))