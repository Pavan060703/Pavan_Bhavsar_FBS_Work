# Write a program to find the longest common prefix of all strings. Use python set
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = ""
    min_len = len(min(strings, key=len))

    for i in range(min_len):
        char_set = set()

        for word in strings:
            char_set.add(word[i])

        if len(char_set) == 1:
            prefix += char_set.pop()
        else:
            break

    return prefix
n = int(input("Enter number of strings: "))
strings = []

for i in range(n):
    strings.append(input("Enter string: "))

result = longest_common_prefix(strings)
print("Longest Common Prefix:", result)
