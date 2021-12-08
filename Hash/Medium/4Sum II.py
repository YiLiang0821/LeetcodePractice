#454
def fourSumCount(nums1, nums2, nums3, nums4):
    m = {}
    answer = 0

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if (nums1[i] + nums2[j]) not in m :
                m[nums1[i] + nums2[j]] = 0
            m[nums1[i] + nums2[j]] += 1
    
    for x in range(len(nums3)):
        for y in range(len(nums4)):
            target = -(nums3[x] + nums4[y])
            if target in m:
                answer += m[target]

    return answer

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