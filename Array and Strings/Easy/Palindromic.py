# 判斷回文
# entire String
def isPalindroms(s):
    n = len(s)
    for i in range( n//2 + 1):  #+1 since index start from 0
        if s[i] != s[n - i -1]:
            return False        # not palindrom then stop
        return True

# sbustring s[l ~ r]
def subIsPalindroms(s, l, r):
    while( l < r):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

# brute force
s ='aaaa'
def findPalindromic(s):
    n = len(s)
    best = ''
    for i in range(n):
        for j in range(i, n):
            if j - i + 1 > len(best) and isPalindroms(s, i, j):
                best = s[i:j+1]
    return best
