# 424
# sliding windows, hash map
from collections import defaultdict
def characterReplacement(s, k):
    ans, start = 0, 0
    count = defaultdict(int)

    for i in range(len(s)):
        count[s[i]] += 1
        
        # check vaild: need to be replaced <= k
        if (i - start + 1) - max(count.values()) > k:
            count[s[start]] -= 1
            start += 1
        ans = max(ans, i - start + 1)
    return ans
