# Python Program to Remove the Given Key from a Dictionary
def removeDict(dict1,key):
    new_dict={}
    for k in dict1:
        if k!=key:

            new_dict[k]=dict1[k]

    return new_dict

dict1={1:"Python",2:"Java",3:"C++"}
key=int(input("Enter the key to remove"))
new_dict=removeDict(dict1,key)
print(new_dict)