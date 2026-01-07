#Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.
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
print("Even Numbers in list are ",even_list)
print("Odd Numbers in list are ",odd_list)


    

