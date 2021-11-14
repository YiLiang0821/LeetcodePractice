def binarySerach(target, arr):
    l, r, search_time = 0, len(arr) - 1, 0
    while l <= r:
        search_time += 1
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid, search_time
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        
    return -1, search_time



def main():
    print('Binary Search')
    arr = [1,2,3,4,5,6]
    target = 5
    print('Array = {0}, target = {1}'.format(arr, target))
    
    result, time = binarySerach(target, arr)
    if result:
        print('Result Index: {0}, search {1} times'.format(result, time))
    else:
        print('No element in the Arry, search {0} times'.format(time))

if __name__ == '__main__':
    main()