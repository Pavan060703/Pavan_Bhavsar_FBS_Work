# Create a function that extracts all the dates from a given text using regular expressions.
# dates can be in various formats like MM/DD/YYYY,DD/MM/YYYY or written out like January 
# 1, 2023. Extract all such date occurrences.
import re

def extract_date(text):
    pattern=r'''\b\d{2}/\d{2}/\d{4}\b|
    \b\d{2}-\d{2}-\d{4}\b|
    \b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\d{4}\b'''

    res=re.findall(pattern,text,re.VERBOSE)
    return res

text="I'm born on July 01,2003."
result=extract_date(text)
print(result)
