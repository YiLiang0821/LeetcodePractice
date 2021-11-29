#204
import math
def countPrimes(n):
    if n < 2:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isPrime[i] == True:
            for j in range(i * 2, n, i):
                isPrime[j] = False
    return sum(isPrime)

print(countPrimes(1001))