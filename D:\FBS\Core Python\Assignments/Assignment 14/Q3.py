# Write a Python Program to find all the unique words and count the frequency of occurrence 
# from a given list of strings. Use python set data type.
def uniqueCount(list_1):
    unique=set(list_1)
    freq={}

    for i in list_1:
        freq[i]=list_1.count(i)

    return unique,freq

list_1=["Python","Java","C++","SQL","Java","Python","Java"]
unique,freq=uniqueCount(list_1)
print("Unique words are ",unique)
print(freq)