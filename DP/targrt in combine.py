'''
判斷 target 是否為組內的和
ref:https://www.youtube.com/watch?v=Jakbj4vaIbE&t=4s
'''
arr = [3, 34, 4, 12, 5, 2]
def rec_subset(arr, i, target):
    if target == 0:
        return True
    elif i == 0:
        return arr[i] == target
    elif arr[i] > target:
        return rec_subset(arr, i - 1, target) #不選的分支
    else:
        choose = rec_subset(arr, i-1, target-arr[i])
        not_choose = rec_subset(arr, i-1, target)
        return not_choose or choose 
print(rec_subset(arr,len(arr)-1, 13))


import numpy as np
def dp_subset(arr, target):
    subset = np.zeros((len(arr), target+1), dtype = bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, target+1):
            if arr[i] > target:
                subset[i, s] = subset[i-1, s]
            else:
                A = subset[i-1, s-arr[i]]
                B = subset[i-1, s]
                subset[i, s] = A or B
    r,c = subset.shape
    return(subset[r-1,c-1])

print(dp_subset(arr,13))
