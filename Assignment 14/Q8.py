# Write a python program to find all the anagrams and group them together from a given
# list of strings.
def anagram(words):
    anagram_dict={}
    for word in words:
        key=''.join(sorted(word))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key]=[word]

    return list(anagram_dict.values())

words=input("Enter words separated by space ").split()
groups=anagram(words)

print("Grouped anagrams")
for group in groups:
    print(group)