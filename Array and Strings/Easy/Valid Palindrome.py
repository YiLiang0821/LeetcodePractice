#125
import re
def isPalindrome(s):
    s = re.sub("[^0-9a-zA-Z]+","",s).lower()
    if s != s[::-1]:
        return False
    return True
#[0-9a-zA-Z] 這段則是找出整個字串中只有小寫字母，大寫字母跟數字