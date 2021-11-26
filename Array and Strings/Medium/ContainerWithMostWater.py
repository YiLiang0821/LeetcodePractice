#11
def ContainerWithMostWater(arr):
    maxArea = 0
    R = len(arr) - 1
    L = 0
    while L < R:
        height = min(arr[R], arr[L])
        length = R - L
        maxArea = max(maxArea, height * length)
        
        if arr[L] < arr [R] :
            L += 1
        else:
            R -= 1
    return maxArea

'''
TC is O(N) due to one loop
SC is O(1), no extra data structure, only use pointer.
'''

print(ContainerWithMostWater([1,2,1]))
