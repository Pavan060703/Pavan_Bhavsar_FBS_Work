#Write a program to input angles of a triangle and check whether triangle is valid or not
angle1=int(input("Enter the first angle of triangle:"))
angle2=int(input("Enter the second angle of triangle:"))
angle3=int(input("Enter the third angle of triangle:"))
sum=angle1+angle2+angle3
if(sum==180 and angle1!=0 and angle2!=0 and angle3!=0):
    print("Triangle is valid")
else:
    print("Triangle is invalid")