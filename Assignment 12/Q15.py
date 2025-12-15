def string_length(s):
    count=0
    for ch in s:
        count+=1
    return count

def larger_string(s1,s2):
    len1=string_length(s1)
    len2=string_length(s2)
    if len1>len2:
        return s1
    elif len2>len1:
        return s2
    else:
        return "Both strings are equal"

s1=input("Enter a string 1 : ") 
s2=input("Enter a string 2 : ") 
result=larger_string(s1,s2)
print(result)  