#Write a program to find sum of all elements of list
def addition_list(li): # defining a function 
    sum=0
    for i in li: # use for loop to traverse each element in list
        sum=sum+i # sum is calculated
    return sum # returning value of sum

li=[23,45,21,56,34,67,78,98]
result=addition_list(li)
print("The sum of all elements of list is ",result)

