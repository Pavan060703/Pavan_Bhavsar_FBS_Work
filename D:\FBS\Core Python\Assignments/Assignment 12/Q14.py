# Python program to count the occurrences of each word in a string.
def countEachWord(string1):
    words=string1.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    return word_count

string1=input("Enter a string : ")
result=countEachWord(string1)
print("Word Occurrences")
for word,count in result.items():
    print(word, " : ",count)
