rows = 5
for i in range(1, rows + 1):
    
    print("  " * (rows - i), end="")
    if i == 1:
        print(1)
    elif i == rows:
        for j in range(1, rows + 1):
            print(j, end="   ")
        print()
    else:
        print(1, end=" ")
        print("    " * (i - 2), end="")   
        print(i)

