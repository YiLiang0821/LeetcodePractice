def maxSum(arr, windowSize):
    arrSize = len(arr)
    if arrSize < windowSize:
        print('Invalid')
        return -1
    elif arrSize == windowSize:
        return sum(arr)
    
    window_sum = sum(arr[i] for i in range(windowSize))
    max_sum = window_sum

    for i in range(arrSize - windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]          #slide the windows. minus front then plus behind
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [80, -50, 90, 100]
k = 2

print(maxSum(arr, k))