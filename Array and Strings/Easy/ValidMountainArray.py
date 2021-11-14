#941
def ValidMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 1
    #check increasing
    while(i < len(arr) and arr[i] > arr[i-1]):
        i += 1
    if(i == len(arr) or i == 1):
        return False

    #check decreasing
    while(i < len(arr) and arr[i] < arr[i-1]):
        i += 1
    return i == len(arr)                        #YES -> True; No -> False
    
    
    
test = [0,1,2,3,4,8,9,10,11,12,11]
print(ValidMountainArray(test))
'''
TC is O(n) -> loop the array one time
SC is O(1) -> no extra space used
'''