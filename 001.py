sum3 = 0
sum5 = 0
sum15 = 0
i = 1
j = 1
k = 1
while((i * 3) < 1000):
    sum3 += i * 3
    i += 1

while((j * 5) < 1000):
    sum5 += j * 5
    j += 1

while((k * 15) < 1000):
    sum15 += k * 15
    k += 1

total = sum3 + sum5 - sum15
print(total)