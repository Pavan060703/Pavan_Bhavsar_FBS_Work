# Write a program to print list after removing even numbers
def removeEven(li):
    odd_li=[]
    for i in li:
        if i%2!=0:
            odd_li.append(i)
    return odd_li
li=[1,2,3,4,5,6,7,8,9,10]
result=removeEven(li)
print(result)