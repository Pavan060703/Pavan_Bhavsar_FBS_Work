def countWords(text):
    char_count=len(text)
    word_count=len(text.split())
    return char_count,word_count

text=input("Enter the string ")
char_count,word_count=countWords(text)
print("Number of characters : ",char_count)
print("Number of words : ",word_count)