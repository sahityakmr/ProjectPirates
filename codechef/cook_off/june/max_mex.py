import sys

dry_run = True
if dry_run:
    file = open('res/max_mex.txt')
    sys.stdin = file

global var
for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [int(i) for i in input().split()]
    smaller_set = set()
    smaller_unique_sum = 0
    ms_count = 0
    for e in arr:
        if e == m:
            ms_count += 1
            continue
        if e < m:
            if e not in smaller_set:
                smaller_set.add(e)
                smaller_unique_sum += e
    if smaller_unique_sum == ((m - 1) * m) / 2:
        print(n - ms_count)
    else:
        print(-1)
    pass
