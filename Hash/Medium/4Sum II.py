#454
from collections import defaultdict
def fourSumCount(nums1, nums2, nums3, nums4):
    m = defaultdict(int)
    ans = 0
    
    for i in nums1:
        for j in nums2:
            diff = 0 - i - j
            m[diff] += 1
    for x in nums3:
        for y in nums4:
            total = x + y
            if total in m:
                ans += m[total]
    return ans

nums1 = [1,2] 
nums2 = [-2,-1] 
nums3 = [-1,2] 
nums4 = [0,2]

print(fourSumCount(nums1, nums2, nums3, nums4))
'''
TC is O(n^2) due to 2 * (loop*loop)
SC is O(n) due to use a map

find out possibility of nums1 + nums2, and put sum as key
check nums3 + nums4, if (nums1 + nums2) - (nums3 + nums4) = 0
'''