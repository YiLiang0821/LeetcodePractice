#278
def firstBadVersion(n):
    L = 1
    R = n
    while(L < R):
        mid = (L + R - 1)//2
        if (not isBadVersion(mid)):
            L = mid + 1
        else:
            R = mid
    return L
'''
TC is O(log n) due to Binary search
SC is O(1) 
'''