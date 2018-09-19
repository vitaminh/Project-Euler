term = 1
prevTerm = 1
sum = 0
while(term < 4000000):
    if term % 2 == 0:
        sum += term
    tempTerm = prevTerm
    prevTerm = term
    term += tempTerm
print(sum)
    