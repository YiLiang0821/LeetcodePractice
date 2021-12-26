#169
def majorityElement(nums):
    m = {}
    for i in nums:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    return max(m, key=m.get) #key=func

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

def majorityElement2(nums):
    m = {}
    for i in nums:
        m[i] = m.get(i, 0) + 1
    for n in nums:
        if m[n] > len(nums) // 2:
            return n
'''
TC, SC are O(n)
'''