'''
Goal: 選出最大不相鄰數字的總和
'''
import time
arr = [1, 2, 4, 1, 7, 8, 3]

def rec_opt(arr, i):  #到i位置的最佳方案
    if i == 0:
        return arr[0]
    elif i == 1 :
        return max(arr[0], arr[1])
    else:
        tmp = rec_opt(arr, i-2) + arr[i]
        tmp_0 = rec_opt(arr, i-1)
        return (max(tmp, tmp_0))
start = time.clock()
print(rec_opt(arr, 6), (time.clock() - start))

def dp_opt(arr):
    opt = [0] * len(arr)
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)): #start from index2
        tmp = opt[i - 2] + arr[i]
        tmp_0 = opt[i - 1]
        opt[i] = max(tmp, tmp_0)
    return(opt[len(arr) - 1]) #返回最後一個數字：len(arr)-1

start = time.clock()
print(dp_opt(arr), (time.clock() - start))
