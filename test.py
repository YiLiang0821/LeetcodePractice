import re
s = "A man, a plan, a canal: Panama"
s= re.sub("[^0-9a-zA-Z]+", '',s)
print(s)