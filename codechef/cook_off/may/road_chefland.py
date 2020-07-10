import math
sum = [0]
counter = 1


def numq(i):
    count = 0
    while i & 1 == 0:
        i = i >> 1
        count += 1
    return 1 << count


for t in range(int(input())):
    n = int(input())
    if math.log2(n) == int(math.log2(n)):
        print(-1)
        continue
    print(numq(i))