def squareCube(li):
    square_list=[]
    cube_list=[]
    for i in li:
        square_list.append(i*i)
        cube_list.append(i*i*i)

    return square_list,cube_list

li=[1,2,3,4,5]
square_list,cube_list=squareCube(li)
print("The elements of list are ",li)
print("The squares of elements of list ",square_list)
print("The cube of elements of list ",cube_list)
