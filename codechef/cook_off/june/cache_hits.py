import sys

dry_run = True
if dry_run:
    file = open('res/cache_hits.txt')
    sys.stdin = file

global var
for t in range(int(input())):
    n, b, m = map(int, input().split())
    start, end = -2, -1
    arr_m = [int(i) for i in input().split()]
    count = 0
    for x in arr_m:
        if dry_run:
            print("x=", x)
        if start <= x <= end:
            if dry_run:
                print("Already loaded")
            pass
        else:
            if (x + 1) % b == 0:
                start = (int((x + 1) / b) - 1) * b
            else:
                start = int((x + 1) / b) * b
            end = min(n - 1, start + b - 1)
            if dry_run:
                print("Loading", start, end)
            count += 1
    print(count)
    pass
