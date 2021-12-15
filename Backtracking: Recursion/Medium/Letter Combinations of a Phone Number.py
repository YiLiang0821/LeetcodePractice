#17
def letterCombinations(digits):
        ans = []
        digitToChar = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'qprs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtrack(index, currChar):
            if len(currChar) == len(digits):
                ans.append(currChar)
                return
            for c in digitToChar[digits[index]]:
                backtrack(index + 1, (currChar + c))
        if digits:
            backtrack(0,"")
        return ans

print(letterCombinations('59'))

'''
TC (n * 4^n), len(digits) = n, 
every time the worst case take 4 letters
'''