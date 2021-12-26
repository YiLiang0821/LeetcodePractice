#204
# sieve of eratosthenes
# check 1 ~ √n 
# a × b = n 4*9 = 36
# a >= √n (9 >= 6)  or b <= √n (4 <= 6)
import math
def countPrimes(n):
    if n < 2:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isPrime[i] == True:
            # If isPrime[i] is a prime number, mark all the multiples as non-prime numbers
            for j in range(i * 2, n, i):
                isPrime[j] = False
    return sum(isPrime)

print(countPrimes(1001))