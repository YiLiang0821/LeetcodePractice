#268
def missingNumber(nums):
    total = (1 + len(nums)) * len(nums) / 2
    current = sum(nums)
    return total - current

nums = [3,0,1]
print(missingNumber(nums))
'''
TC is O(n) --> sum()
SC is O(1)
'''