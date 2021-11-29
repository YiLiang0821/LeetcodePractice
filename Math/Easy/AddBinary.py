#67
def addBinary(a, b):
    result = []
    carry = 0
    lengthA = len(a) - 1
    lengthB = len(b) - 1

    while lengthA >= 0 or lengthB >= 0 or carry > 0:
        total = carry
        if lengthA >= 0:
            total = total + int(a[lengthA])
            lengthA -= 1
        if lengthB >= 0:
            total = total + int(b[lengthB])
            lengthB -= 1
            
        result.append(str(total%2))
        carry = total // 2
    return (''.join(reversed(result)))


a = "1010" 
b = "1011"
print(addBinary(a, b))

'''
TC is O(n), n is the maximun length of the 2 input strings
SC is O(n), create an array 
'''