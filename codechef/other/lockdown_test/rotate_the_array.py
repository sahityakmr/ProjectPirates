dry_run = False
T = 1
n, d = 10, 2
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if not dry_run:
    T = int(input())
for t in range(T):
    if not dry_run:
        n, d = map(int, input().split())
        arr = [int(i) for i in input().split()]
    t_arr = arr[0:d]
    for i in range(n - 1, d - 1, -1):
        arr[(i + d) % n] = arr[i]
    for i in range(d):
        arr[(i + d) % n] = t_arr[i]
    print(*arr, sep=' ')
