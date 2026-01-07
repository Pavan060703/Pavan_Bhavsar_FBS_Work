# Write a program to find sum of digits using recursion
def sum_of_digit(num):
    if num<=0:
        return 0
    else:
        return (num%10) + sum_of_digit(num//10)
num=int(input("Enter the number"))
result=sum_of_digit(num)
print(result)