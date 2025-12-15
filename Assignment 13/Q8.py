#Python Program to count the frequency of words appearing in a string using a dictionary.

def frequency_words(s):
    words=s.split()
    count={}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1

    return count

s=input("Enter a string : ")
result=frequency_words(s)
for word,count in result.items():
    print(word," : ",count)