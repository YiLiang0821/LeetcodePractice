#5
def isPaliString(s, l, r):
    while(0 <= l and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[l+1:r] # s[l] == s[r] then l--, r++
def longestPalindrome(s):
    res = ''
    for i in range(len(s)):
        oddRes = isPaliString(s, i, i)
        evenRes = isPaliString(s, i, i + 1)

        tmpRes = ''
        tmpRes = oddRes if len(oddRes) > len(evenRes) else evenRes
        res = tmpRes if len(tmpRes) > len(res) else res
    return res


s = "babad"