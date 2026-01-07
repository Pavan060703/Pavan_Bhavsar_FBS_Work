# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
def max_product_pair(nums):
    nums_set = set(nums)  
    nums_list = list(nums_set)
    max_product = None
    pair = ()

    n = len(nums_list)

    for i in range(n):
        for j in range(i + 1, n):
            product = nums_list[i] * nums_list[j]

            if max_product is None or product > max_product:
                max_product = product
                pair = (nums_list[i], nums_list[j])

    return pair, max_product
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
pair, product = max_product_pair(numbers)
print("Numbers with maximum product:", pair)
print("Maximum product:", product)
