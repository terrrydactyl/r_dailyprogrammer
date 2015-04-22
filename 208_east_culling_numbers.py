# Trivial solution, but doesn't retain order of items
def set_culling(nums):
    return list(set(nums))

###############################################################################


# Keeps the order, but expensive as it tries to find the duplicate each time.
# which makes this O(n^2).
def list_culling(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique

###############################################################################

from collections import Counter


# Solution implementing Counter, but still doesn't retain order.. overly
# complicated solution.
def counter_culling(nums):
    unique = Counter(nums)
    return [key for key in unique]

input = raw_input("Enter numbers: ")
nums = input.split()
print list_culling(nums)
