# Write a python program to find all the unique combinations of 3 numbers from a give list
# of numbers , adding up to a target number.
def three_sum(nums,target):
    result=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==target:
                    triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                    result.add(triplet)

    return result

nums=list(map(int,input("Enter separated by space :").split()))
target=int(input("Enter target sum"))
triplets=three_sum(nums,target)
print("Unique Combinations:")
for t in triplets:
    print(t)
                                  
                    