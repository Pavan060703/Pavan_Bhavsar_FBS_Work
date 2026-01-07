# Python program to sort a list according to the length of the elements in a list
def BubbleSortExample(li):
    n=len(li)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(str(li[j]))>len(str(li[j+1])):
                li[j],li[j+1]=li[j+1],li[j]
    return li

li=[345,32,5675,1,89087]
result=BubbleSortExample(li)
print(result)