#To find Minimum element in a list
def min_element(li): # defined function         
    min=li[0] # declared min as a first element of list
    for i in li: # traverse each element in list
        if i<min: #check conditon if element is less than min element then go inside loop
            min=i # that i value stored in min variable 
    return min # return min value

li=[43,56,23,45,41,10]
result=min_element(li)
print("The minimum element in list is ",result)