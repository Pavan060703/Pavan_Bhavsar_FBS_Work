# Write a program to create three lists of numbers , their squares and cubes
def squareCube(li):
    square_li=[]
    cube_li=[]
    for i in li:
        square_li.append(i*i)
        cube_li.append(i*i*i)
    return square_li,cube_li

li=[1,2,3,4,5]
square_li,cube_li=squareCube(li)
print(li)
print(square_li)
print(cube_li)