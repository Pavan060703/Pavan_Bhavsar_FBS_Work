# Define a function that takes a text and a list of forbidden words. Replace all occurrences 
#of these forbidden words with asterisks (*) using regular expressions. 
import re
def function_regex(text,forbidden_words):
    for word in forbidden_words:
        pattern=r'\b'+word+r'\b'
        stars='*' * len(word)
        text=re.sub(pattern,stars,text,flags=re.IGNORECASE)
    return text

text='Python and Java are popular languages. Java is widely used.'
forbidden_words=['java','python']

output=function_regex(text,forbidden_words)
print(output)