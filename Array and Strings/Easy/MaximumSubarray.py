#coding=utf-8
#53
# largest sum = total - smallest sum
def maxSubArray2(nums):
    totalSum = 0
    minSum = 0
    maxSum = float('-inf')  #"-無限大" 的用法
    for i in nums:
        totalSum += i
        if (totalSum - minSum > maxSum):
            maxSum = totalSum - minSum
        # when i is negative
        if totalSum < minSum:
            minSum = totalSum
    return maxSum
# if current item is bigger than post-sumArray, then can discard post-sumArray
def maxSubArray(nums):
    if not nums:
        return 0
    currentSum = nums[0]
    maxSum = nums[0]
    for i in nums[1:]:
        currentSum = max(i, currentSum + i) # check subarray whether continue to accumulate
        maxSum = max(maxSum, currentSum)    # pick max subarray
    return maxSum




nums = [1,2,-6,3,4,5]
print(maxSubArray(nums))
