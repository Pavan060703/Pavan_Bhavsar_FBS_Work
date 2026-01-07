#Python Program to Find the Second Largest Number in a List Using Bubble Sort
def BubbleSortExample(li):
    n=len(li)
    for i in range(n):
        for j in range(0,n-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li

li=[12,43,56,31,10,14]
result=BubbleSortExample(li)
print(result[-2])
