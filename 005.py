
def evenDiv(n):
    for i in range(11, 21):
        if n % i != 0:
            return False
    return True

def findNum():
    i = 2520
    while(evenDiv(i) == False):
        i += 2520
    return i

print(findNum())