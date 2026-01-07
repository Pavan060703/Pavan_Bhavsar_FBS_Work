#Write a program to remove duplicates from the list
def remove_duplicates(li):
    unique_list = []
    
    for item in li:
        found = False
        for u in unique_list:
            if u == item:
                found = True
                break
        
        if not found:
            unique_list.append(item)
    
    return unique_list



li = [10,20,30,40,50,60,60,70,60]
result = remove_duplicates(li)
print(result)


