# 33
# require O(log n)
def search(nums, target):
    l, r = 0, len(nums) - 1
    while (l <= r):
        m = (l + r) // 2
        if nums[m] == target:
            return m
        # in the left side
        if nums[l] <= nums[m]:
            # still in left side
            if nums[l] <= target <= nums[m]:
                r = m - 1
            # need to search right side
            else:
                l = m + 1
        else:
        # in the right side
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

nums = [3,1]
target = 1
print(search(nums, target))
'''
TC is O(log n) due to binary search
'''
