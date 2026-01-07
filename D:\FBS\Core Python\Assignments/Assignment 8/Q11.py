def isArmStrong(num):
    temp=num
    length=len(str(num))
    total=0

    while temp>0:
        digit=temp%10
        total=total+(digit**length)
        temp=temp//10

    if total==num:
        print("Armstrong number")
    else:
        print("Not Armstrong number")
n=int(input("Enter the number"))
isArmStrong(n)