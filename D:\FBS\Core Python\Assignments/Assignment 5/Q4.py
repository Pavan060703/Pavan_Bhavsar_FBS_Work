num=int(input("Enter a number"))
original_num=num
count_digits=0
temp=num
while temp>0:
    temp=temp//10
    count_digits+=1

temp=num
sum_Armstrong=0

while temp>0:
    digit=temp%10
    power=1

    for i in range(count_digits):
        power=power*digit
    
    sum_Armstrong+=power
    temp=temp//10

if sum_Armstrong==original_num:
    print(original_num," is an armstrong number")
else:
    print(original_num," is not armstrong number")
    