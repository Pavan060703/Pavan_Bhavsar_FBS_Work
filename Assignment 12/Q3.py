# Python program to detect if two strings are Anagrams.
def anagram(s1,s2):
    s1.replace(" ","").lower()
    s2.replace(" ","").lower()
    if sorted(s1)==sorted(s2):
        return f"These strings are anagrams."
    else:
        return f"These strings are not anagrams."
    
s1=input("Enter string 1")
s2=input("Enter string 2")
result=anagram(s1,s2)
print(result)

