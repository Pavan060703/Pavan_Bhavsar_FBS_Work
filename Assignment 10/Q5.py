def search_ele(li,ele):
    count=0
    for i in li:
        if i==ele:
            count+=1
    return count

li=[12,23,54,55,67,78]
ele=int(input("Enter the element to be search"))

count=search_ele(li,ele)

if count>0:
    print(ele, "is present in the list")
    print("It will occur in the list ",count,"Times")
else:
    print(ele, "is not present in the list")