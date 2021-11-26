#34 # require TC O(log n)
def searchRange(nums, target):
    try:
        head = nums.index(target)
        return [head, head + nums.count(target) - 1]
    except:
        return [-1, -1]

    
nums = [5,7,7,8,8,10]
target = 6

print(searchRange(nums, target))

'''
index() TC is O(n) -> x in list operation
count() TC is O(n)
'''

# solution 2
# sorted -> think binary search first
# find first and last position
def findFirst(nums, target):
    L = 0
    R = len(nums) - 1
    while (L <= R):
        mid = (L + R) // 2
        if nums[mid] == target:
            if (mid == 0 or nums[mid - 1] != target):
                return mid
            R = mid - 1             # not the first
        elif nums[mid] > target:
            R = mid - 1
        else:
            L = mid + 1
    return -1
def findLast(nums, target):
    L = 0
    R = len(nums) - 1
    while (L <= R):
        mid = (L + R) // 2
        if nums[mid] == target:
            if (mid == len(nums) - 1 or nums[mid + 1] != target):
                return mid
            L = mid + 1             # not the last
        elif nums[mid] > target:
            R = mid - 1
        else:
            L = mid + 1
    return -1
print([findFirst(nums, target), findLast(nums, target)])
'''
TC is O(log n) due to binary search 
SC is O(1) no additional memory(space), only ponitor and it's constant 
'''