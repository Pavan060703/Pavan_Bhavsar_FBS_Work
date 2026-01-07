# Write a program to solve the following series :
# b. b. N + N^2 + N^3+N^4 .....+N^N 
n=int(input("Enter the value of N:"))
sum_series=0
for i in range(1,n+1):
    power=1
    for j in range(i):
        power=power*n

    sum_series+=power

print("Sum of the series ",sum_series)