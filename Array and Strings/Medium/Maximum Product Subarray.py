#152
# DP
def maxProduct(nums):
    # if only one element
    ans = max(nums)
    curMin, curMax = 1, 1
    # encounter 0 -> spilt two subarray [...],0,[...] no impact due to ans store the previous max subarray
    for i in nums:
        temp = (i * curMax, i * curMin, i) # i is because temp: (-,-,+) or (+,+,-)
        curMax = max(temp)
        curMin = min(temp)
        ans = max(ans, curMax)
    return ans


nums = [2,3,-2,4]
print(maxProduct(nums))
