# Python Program to merge two lists and sort it.
def mergeList(li_1,li_2):
    new_list=li_1+li_2
    new_list.sort()
    return new_list

li_1=[1,3,5,7,9]
li_2=[2,4,6,8,10]
new_list=mergeList(li_1,li_2)
print("The sorted list ",new_list)
    