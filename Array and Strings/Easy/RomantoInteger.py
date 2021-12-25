#13
def RomantoInteger(s):
    mapValue = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        tmpV = mapValue[s[i]]
        if i != 0 and mapValue[s[i - 1]] < mapValue[s[i]]:
            # - 2 *() 需要多減前一次加進去result的 CM = 100(C) + 1000(M) -> 900(CM)
            tmpV = tmpV - 2 * mapValue[s[i - 1]]
        result += tmpV
    return result
s = "MCMXCIV"
print(RomantoInteger(s))

'''
TC is O(n)
SC is O(n)
A hashtable typically has a space complexity of O(n).
'''