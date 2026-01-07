# Write a python program that finds all pairs of elements in a list whose sum is equal 
# to a given value.

def pairsEle(li,target):
    pairs=[]
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]+li[j]==target:
                pairs.append((li[i],li[j]))

    return pairs

li=[10,20,30,40,50]
target=50
result=pairsEle(li,target)
print(result)