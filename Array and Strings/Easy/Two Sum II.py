#167
# numbers is a sorted array
def twoSum2(numbers, target):
    l, r = 0, len(numbers)-1
    while(l < r):
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return None

numbers = [2,3,4]
target = 6
print(twoSum2(numbers, target))