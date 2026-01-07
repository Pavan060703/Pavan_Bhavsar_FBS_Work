# Python program to check if a key exists in a dictionary
def check_key(dict1,key):
    for k in dict1:
        if k==key :
            return True
    return False
    
my_dict1={1:"Python",2:"Java",3:"C++"}
key=int(input("Enter the key"))
if check_key(my_dict1,key):
    print("Key exists")
else:
    print("Key not exists")