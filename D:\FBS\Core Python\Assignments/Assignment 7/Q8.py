n = 5

for i in range(1, n+1):

    # Left side increasing numbers
    for j in range(1, i+1):
        print(j, end=" ")

    # Middle spaces
    spaces = (n - i) * 4
    print(" " * spaces, end="")

    # Right side decreasing numbers (start from i-1 to avoid duplicate)
    for j in ṇrange(i-1, 0, -1):
        print(j, end=" ")

    print()
