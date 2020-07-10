import math


def get_factor(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return int(x / i)
    return 1


for t in range(int(input())):
    x, k = map(int, input().split())
    count = 0
    res = 0
    while x > 1:
        x = get_factor(x)
        count += 1
        if count == k or (count == (k - 1) and x > 1):
            res = 1
            break
    print(res)
