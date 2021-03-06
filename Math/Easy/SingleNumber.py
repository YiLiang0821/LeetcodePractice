#136
def singleNumber(nums):
    return 2 * sum(set(nums)) - sum(nums)
'''
TC is O(2 * n) = O(n) sum twice; 
set() is kind of hash so using set take O(n) -> iterate over list
SC is O(n) due to the usage of set
''' 