#278
# Binary Search
def firstBadVersion(n):
    if n == 1:
        return 1
    L = 1
    R = n
    while(L < R):
        mid = (L + R - 1)//2 # list index start from 0
        if (not isBadVersion(mid)):
            L = mid + 1
        else:
            R = mid # all are bad after mid
    '''
    while(L < R):
            mid = (L + R) //2
            if isBadVersion(mid) and isBadVersion(mid-1) is False:
                return mid
            elif isBadVersion(mid):
                R = mid - 1
            else:
                L = mid + 1
    '''
    return L
'''
TC is O(log n) due to Binary search
SC is O(1) 
'''