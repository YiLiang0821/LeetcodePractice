#217
#will use hash for practice
def containsDuplicate(nums):
    m = {}
    for i in nums:
        if i in m:
            return True
        else:
            m[i] = 1
    return False
'''
TC is O(n) -> a loop
SC is O(n) -> create a Map
'''