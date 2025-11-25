#write a program to reverse the list
def reverse_list(li):
    li_1=li[-1::-1]
    return li_1
li=[12,43,34,23,4,5,6]
result=reverse_list(li)
print(result)