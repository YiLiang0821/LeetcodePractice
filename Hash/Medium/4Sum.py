# 18
from collections import defaultdict
def fourSum(nums, target):
    nums.sort()
    if not nums or len(nums) < 4:
        return []
    m = defaultdict(list)
    res = set()

    for num1 in range(len(nums) - 1):
        for num2 in range(num1 + 1, len(nums)):
            diff = target - nums[num1] - nums[num2]
            m[diff].append((num1, num2))
    for x in range(len(nums) - 1):
        if x > 0 and nums[x] == nums[x-1]:
            continue
        for y in range(x+1, len(nums)):
            if y > x + 1 and nums[y] == nums[y-1]:
                continue
            total = nums[x] + nums[y]
            if total in m:
                for pair in m[total]:
                    # need to exclude the case pair[0] or pair[1] is num1 or num2
                    if pair[0] > y:
                        res.add((nums[x], nums[y],nums[pair[0]], nums[pair[1]]))
    return [list(l) for l in res]

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))