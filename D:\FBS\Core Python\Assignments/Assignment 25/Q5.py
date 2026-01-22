# #Write a Python function that takes an email address as input and uses a regular
# expression to validate if it is a valid email address. The function should return True for
# valid emails and False for invalid ones.
import re
def validate_email(text):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern,text))

text='pavanbhavsar2003@gmail.com'

result=validate_email(text)
print(result)