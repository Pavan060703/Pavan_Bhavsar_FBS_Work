# Python program to put Even and Odd elements of a list into two Different Lists.
def evenOdd(li):
    even_list=[]
    odd_list=[]
    for i in li:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list

li=[1,2,3,4,5,6,7,8,9,10]
even_list,odd_list=evenOdd(li)
print("Even Numbers are ",even_list)
print("Odd Numbers are",odd_list)