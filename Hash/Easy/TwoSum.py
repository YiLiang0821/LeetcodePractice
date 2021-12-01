#1
def twoSum(nums, target):
    ref = {}
    for i, char in enumerate(nums):
        if (target - char) in ref:
            return([ref[(target - char)], i])
        else:
            ref[char] = i


nums = [3,2,4]
target = 6
      
print(twoSum(nums, target))

'''
TC is O(n) -> a loop

SC is O(n) -> create a Map
'''