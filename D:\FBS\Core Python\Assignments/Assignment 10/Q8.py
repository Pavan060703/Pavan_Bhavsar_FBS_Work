#Write a program to create a duplicate of an existing list. It should not point to same list.
def duplilist(li):
    list_duplicate=[]
    for i in li:
        list_duplicate.append(i)
    
    # print(id(list_duplicate))
    # print(id(li))
    return list_duplicate

li=[10,20,30,40,50,60]
result=duplilist(li)
print(result)
