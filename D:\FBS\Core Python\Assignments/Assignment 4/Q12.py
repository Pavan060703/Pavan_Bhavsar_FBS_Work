num=int(input("Enter the number"))
number=num
digit=0
sum=0
length=len(str(num))
for i in range(length):
    digit=int(num%10)
    num=num/10
    sum+=pow(digit,length)

if sum==number:
    print("armstrong")
else:
    print("Not armstrong")