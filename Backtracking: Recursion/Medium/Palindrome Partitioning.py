#131
from typing import List
class Solution:
    def isPail(self, l, r):
        while(l < r):
            if self.s[l] != self.s[r]:
                return False
            l += 1
            r -= 1
        return True
    def backTrack(self, cur, index):
        # end case, index out of bound
        if index == len(self.s):
            self.ans.append(cur[:])
            return
        for j in range(index, len(self.s)):
            #[0:0](a), [0:1](aa), [0:2](aab)
            if self.isPail(index, j):
                cur.append(self.s[index:j+1])
                self.backTrack(cur, j+1)
                cur.pop()
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.ans = []
        self.backTrack([], 0)
        return self.ans

s = "aabcd"
s = Solution()
print(s.partition(s))
'''
Brust force: backtracking
O(2^n) 
'''