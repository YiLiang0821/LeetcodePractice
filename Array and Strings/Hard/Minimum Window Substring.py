# 76
# sliding wiondows
# hash
from collections import defaultdict
def minWindow(s, t):
    # edge case
    if t == '':
        return ''
    
    # set up hash map t
    countT = defaultdict(int)
    for i in t:
        countT[i] += 1
    need = len(countT)
    
    # prepare windows
    windows = defaultdict(int)
    have = 0
    res = [-1, -1]
    length = float('inf')
    start = 0

    for end in range(len(s)):
        char = s[end]
        windows[char] += 1

        # update have if meet condition
        if char in countT and windows[char] == countT[char]:
            have += 1
        
        # check have == need -> find substring
        while have == need:
            # update res is shorter
            if (end - start + 1) < length:
                res = [start, end]
                length = end - start + 1
            # pop out from start
            windows[s[start]] -= 1
            if s[start] in countT and windows[s[start]] < countT[s[start]]:
                have -= 1
            start += 1
    start, end = res
    return s[start:end+1] if length != float('inf') else ''

s = "bbaa"
t = "aba"
print(minWindow(s, t))

'''
TC is O(n)
'''