#287
# Constrain: constant extra space O(1) and can't modify the array
# Floyd's Algo
def findDuplicat(nums):
    slow = 0
    fast = 0
    # Take the number in the array as the index of next node.
    # until intersect: first meeting point
    # need to add once first since they both start at 0
    while True:
        # v = next index
        slow = nums[slow]
        # faster two times
        fast = nums[nums[fast]]
        if slow == fast:
            break
        # set fast to the begin point 0
        # this time both walk same distance
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
    return slow

'''
index will be 0 ~ n, nums[0] is the begin, and the index 1 ~ n are the value map to
array's value can be see as the index that value appear
'''