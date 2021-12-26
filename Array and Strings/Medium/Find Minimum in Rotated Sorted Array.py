# 153

def findMin(nums):
    res = nums[0]
    l = 0
    r = len(nums) - 1
    while (l <= r):
        # if in sorted subarray
        # nums[l] always will be the smallest in sorted subarray
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        # not in sorted subarray
        m = (l + r) // 2
        # the minimun so far
        res = min(res, nums[m])
        if nums[l] <= nums[m]:
            # search right
            l = m + 1
        else:
            r = m - 1
    return res
