#Write a program to create a new list from existing list which contains cube of each number of list
def cube_list(li):
    cube_li=[]
    for i in li:
        cube_li.append(i*i*i)

    return cube_li

li=[1,3,4,5,6]
result=cube_list(li)
print(result)