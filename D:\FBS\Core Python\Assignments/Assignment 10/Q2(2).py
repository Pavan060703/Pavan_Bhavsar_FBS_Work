def max_element(li):
    max=li[0]
    for i in li:
        if i>max:
            max=i
    return max

li=[32,45,21,56,76,40,23,12,54,32]
result=max_element(li)
print("The maximum element in list is",result)