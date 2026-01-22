# Write a function that extracts all the URLs from a given text using regular expressions.
# Return a list of URLs found in the input text.

import re
def extract_url(text):
    pattern=r'(https?://\S+|www\.\S+)'
    urls=re.findall(pattern,text)

    return urls

text="Check once www.google.com"
result=extract_url(text)
print(result)