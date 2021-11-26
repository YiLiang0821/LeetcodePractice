#14
def longestCommonPrefix(strs):
    s1 = max(strs)
    s2 = min(strs)
    for i, char in enumerate(s1):
        if char != s2[i]:
            return s1[ : i]
    return s1
'''
TC is O(N) due to only one loop O(n) + max O(n) + min O(n) = O(3n) -> O(n)
SC is O(1) only use point to value
max(), min() usually are O(n)
'''