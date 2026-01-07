#Write a program to print list after removing even numbers.
def removeEven(li):
    new_list=[]
    for i in li:
        if i%2!=0:
            new_list.append(i)
    return new_list

li=[1,2,3,4,5,6,7,8,9,10]
result=removeEven(li)
print("After removing even numbers ",result)