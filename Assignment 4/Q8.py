start=int(input("Enter the starting number of the range"))
end=int(input("Enter the ending number of the range"))
for i in range(start,end+1):
    if i%7==0:
        if i%5==0:
            print(i)

