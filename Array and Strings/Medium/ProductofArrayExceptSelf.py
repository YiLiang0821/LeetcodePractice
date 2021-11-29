#238
def productExceptSelf(nums):
    if nums.count(0) > 1:
        return [0 for _ in range(len(nums))]
        
    # only one zero in the list
    total = 1
    zeroIndex = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroIndex = i
            continue
        total = total * nums[i]
    for n in range(len(nums)):
        if zeroIndex < 0:
            nums[n] = total // nums[n]
        else:
            if n == zeroIndex:
                nums[n] = total
            else:
                nums[n] = 0
    return nums
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))  

def productExceptSelf2(nums):
    length = len(nums)
    pre = 1
    post = 1
    res = [1] * length
    
    # front
    for i in range(length):
        res[i] = res[i] * pre
        pre = pre * nums[i]
    # backward
    for j in range(length - 1, -1, -1):
        res[j] = res[j] * post
        post = post * nums[j]
    return res