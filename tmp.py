'''
arr = [1,1,2,4,5,1,6]
a = [1,2]
(x for x in arr if x not in a) #生成器
print(list((x for x in arr if x not in a)))

def allEven():
    n = 2
    while True:
        yield n
        n += 2
even = allEven() #函數生成器
print(next(even))
print(next(even))
print(next(even))
'''
def reverse(x: int) -> int:
        if x == 0:
            print(0)
        elif x < 0:
            print(-1 * (int(str(-x)[::-1])))
        else:
            print((int(str(x)[::-1])))
reverse(-123)