num=int(input("Enter the number"))
temp=num
reversed_number=0

while temp>0:
    digit=temp%10
    reversed_number=(reversed_number*10)+digit
    temp=temp//10

if num==reversed_number:
    print("Palindrome")
else:
    print("Not Palindrome")