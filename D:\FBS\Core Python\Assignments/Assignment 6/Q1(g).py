for i in range(1, 6):
    print("  " * (5 - i), end="")
    ch=ord('A')
    for j in range(1, 2 * i):
        print(chr(ch), end=" ")
        ch += 1
    print()
