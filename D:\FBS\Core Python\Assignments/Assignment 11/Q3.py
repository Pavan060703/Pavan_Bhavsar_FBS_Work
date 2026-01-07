# Python program to sort the list according to the Second Element in Sublist
def get_second(ele):
    return  ele[1]
def sort_second(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if get_second(li[i])>get_second(li[j]):
                li[i],li[j]=li[j],li[i]
    return li

li=[[10,2],[5,1],[4,3]]
result=sort_second(li)
print(result)