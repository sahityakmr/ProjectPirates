t = int(input())
while t > 0:
    n = int(input())
    min = 10000000000
    for i in range((int(n / 2)), 0, -1):
        if n % i == 0:
            r = n / i
            val = abs(r - i)
            if min > val:
                min = val
            else:
                break
    print(int(min))
    t = t - 1
