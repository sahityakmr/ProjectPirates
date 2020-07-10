t = int(input())
while t > 0:
    n, k = map(int, input().split())
    if k != 0:
        print(int(n / k), int(n % k))
    else:
        print(int(0), int(n))
    t = t - 1
