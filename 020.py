import math

def findSum(n):
    sum = 0
    x = math.factorial(n)
    while n > 0:
        sum += x % 10
        x /= 10
    return sum

print(findSum(100))