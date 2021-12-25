#283
def MoveZeron(arr):
    j = 0
    for item in arr:
        if item != 0:
            arr[j] = item
            j += 1
    for x in range(j, len(arr)):
        arr[x] = 0
    return arr
    '''
    # this needs to create another array
    nums =[0 for _ in range(len(arr))]
    for item in (arr):
        if item != 0:
            nums[j] = item
            j += 1
    return nums
    '''

print(MoveZeron([1, 0, 0, 3, 10, 0, 0, 15]))
'''
This is O(N), since it has 2 O(N) -> O(2*N) -> O(N)
'''