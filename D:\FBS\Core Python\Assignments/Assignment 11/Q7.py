# Python Program to Find the intersection of Two Lists.
def intersection(li1,li2):
    inter=[]
    for i in li1:
        if i in li2:
            inter.append(i)
    return inter

li1=[1,2,3,4,5]
li2=[1,3,5,6,7]
result=intersection(li1,li2)
print(result)