# Develop a function that counts the occurrences of each word in a given text. Use regular
#expressions to split the text into words and then count the frequency of each word.
import re
def count_occurrences(text):
    text=text.lower()

    words=re.findall(r'\b\w+\b',text)

    count={}

    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1

    return count

text="Python is an Object Oriented Programming Language."
result=count_occurrences(text)
print(result)




