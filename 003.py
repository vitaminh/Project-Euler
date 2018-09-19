import math

def maxPrimeFactor(n):

    maxPrime = -1

    # Divide by two to get odd number
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1     # n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n

    return int(maxPrime)

print(maxPrimeFactor(600851475143))