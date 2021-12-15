#131
def isPali(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def backTrack(ans, partition, s, index):
    # end case, index out of bound
    if index >= len(s):
        ans.append(partition[:])
        return

    for j in range(index, len(s)):
        #[0:0](a), [0:1](aa), [0:2](aab)
        if isPali(s, index, j):
            partition.append(s[index: j+1])
            backTrack(ans, partition, s, j + 1)
            partition.pop()

def partition(s):
    ans = []
    partition = []
    backTrack(ans, partition, s, 0)
    return ans

s = "aab"
print(partition(s))
'''
Brust force: backtracking
O(2^n)
'''