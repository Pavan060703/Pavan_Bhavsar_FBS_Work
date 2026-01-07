n = 5

for i in range(1, n+1):
    if i == 1:
        for j in range(1, n+1):
            print(j, end=" ")
        print()
    else:
        print(i, end=" ")
        for s in range(n - i - 1):
            print(" ", end="  ")
        
        if i != n:
            print(i if False else 5)   
        else:
            print()  
