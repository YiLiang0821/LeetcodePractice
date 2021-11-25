#3
s = "pwwkew"
def LongestSubstringWithoutRepeatingCharacters(s):
    if not s:
        return 0
    recordMAp = {}
    L, R = 0, 0
    ans = 0
    while (R < len(s)):
        if s[R] in recordMAp:
            L = max(L, recordMAp[s[R]] + 1)
        recordMAp[s[R]] = R

        ans = max(ans, R - L + 1)
        R += 1
    return ans

print(LongestSubstringWithoutRepeatingCharacters(s))

def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
                return (0)
        dic, ans, start = {}, 0, 0
        for i, char in enumerate(s):
            if char in dic : 
                start = max(start, dic[char] + 1)           
            dic[char] = i
            ans = max (ans, i - start + 1)   
        return ans
'''
TC is O(N) due to only one loop over array
SC is O(N) create a Map and Map SC is O(N)
'''