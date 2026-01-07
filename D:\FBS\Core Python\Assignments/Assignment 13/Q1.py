# Python program to add key-value pair to the Dictionary
def add_key_value(d,key,value):
    d[key]=value
    return d

my_dict={}
key=input("Enter key : ")
value=input("Enter value : ")
result=add_key_value(my_dict,key,value)
print("Updated Dictionary : ",result)