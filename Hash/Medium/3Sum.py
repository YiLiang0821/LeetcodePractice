def threeSum(nums):
    answer = []
    nums = sorted(nums)

    for i, item in enumerate(nums):
        if i > 0 and nums[i-1] == item:
            continue
        l = i + 1
        r = len(nums) - 1
        while (l < r):
            if item + nums[l] + nums[r] < 0:
                l += 1
            elif item + nums[l] + nums[r] > 0:
                r -= 1
            else:
                answer.append([item, nums[l], nums[r]])
                l += 1
                while(l < r and nums[l] == nums[l - 1]):
                    l += 1
    return answer

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

'''
TC is sorted: O(n log n) + O(n^2) => O(n^2)
SC is O(n) due to sorting
'''