#write a program to remove all occurrences of a given element in the list.
def dupli(li,ele):
    new_list=[]
    for i in li:
        if ele!=i:
            new_list.append(i)
    return new_list

li_1=[10,20,30,40,50,60,60]
ele_1=int(input("Enter the element to remove"))
print(dupli(li_1,ele_1))



