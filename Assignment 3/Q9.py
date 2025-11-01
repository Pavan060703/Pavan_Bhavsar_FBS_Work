sub1=int(input("Enter the marks of first subject"))
sub2=int(input("Enter the marks of second subject"))
sub3=int(input("Enter the marks of third subject"))
sub4=int(input("Enter the marks of fourth subject"))
sub5=int(input("Enter the marks of fifth subject"))
total=sub1+sub2+sub3+sub4+sub5
percentage=total/5
if(percentage>=85):
    print("First Class")
elif(percentage>=75):
    print("Second Class")
elif(percentage>=60):
    print("Third Class")
elif(percentage>=35):
    print("Fourth Class")
else:
    print("Failed")