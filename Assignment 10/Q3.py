# Write a program to find the second largest element in the list
def second(li):
    largest = li[0]
    second_largest = li[0]
    for i in li:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest

li=[32,45,23,76,5,67]
result=second(li)

print("Second largest element is:", result)