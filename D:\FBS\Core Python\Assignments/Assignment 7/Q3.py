rows=5
for i in range(1, rows + 1):
    if i == rows:
        for j in range(1, rows + 1):
            print(j, end=" ")
    else:
        print(1, end=" ")
        if i > 1:
           print("  " * (i - 2), end="")
           print(i, end="")
    print()
