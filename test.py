class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def backTrack(self, ans, partition, s, index):
        if index >= len(s):
            ans.append(partition[:])
            return
        for j in range(index, len(s)):
            if self.isPalindrome(s, index, j):
                partition.append(s[index: j+1])
                self.backTrack(ans, partition, s, j+1)
                partition.pop()
        
    def partition(self, s):
        ans = []
        partition = []
        self.backTrack(ans, partition, s, 0)
        return ans
s=Solution()
print(s.partition('aab'))