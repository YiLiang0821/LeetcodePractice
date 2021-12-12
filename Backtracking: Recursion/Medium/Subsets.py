#78


def subsets(nums):
    ans = []
    subset = []
    
    def backtrack(i):
        if (i >= len(nums)):
            ans.append(subset[:])
            return
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()
        backtrack(i+1)
        
    backtrack(0)
    return ans
    
nums = [1,2,3]
print(subsets(nums))


'''
subset: each element has two option: take or not to take
so nums got 2^n subsets, n is len(nums)

total 2^n subsets
and each subset could be up to n elements
TC will be O(n * 2^n)
'''