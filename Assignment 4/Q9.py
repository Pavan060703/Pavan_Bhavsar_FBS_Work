start=int(input("Enter the starting number of range"))
end=int(input("Enter the ending number of range"))
num=int(input("Enter the number which check divisible by or not"))
for i in range(start,end+1):
    if i%num==0:
        print(i)