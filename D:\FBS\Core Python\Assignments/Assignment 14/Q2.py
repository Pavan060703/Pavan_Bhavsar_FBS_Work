def removeEle(set1,set2):
    set1.difference_update(set2)
    return set1

set1={10,20,30,40,50,60}
set2={20,30,50}

print(removeEle(set1,set2))