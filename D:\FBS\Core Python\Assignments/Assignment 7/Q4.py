for i in range(1,6):
    print("  " * (6 - i), end="")
    for j in range(i, i + i):
        print(j, end=" ")
    for j in range(i + i - 2, i - 1, -1):
        print(j, end=" ")
    print()
