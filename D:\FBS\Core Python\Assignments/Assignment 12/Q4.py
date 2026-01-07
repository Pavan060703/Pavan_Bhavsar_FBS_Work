# Python program to form a new string where the first character and the last character have been exchanged.
def exchangeString(s):
    if len(s)<=1:
        new_str=s
    else:
        new_str=s[-1]+s[1:-1]+s[0]
    
    return new_str

s=input("Enter the string")
result=exchangeString(s)
print(result)

        
