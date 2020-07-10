ids = []
n, k = 0, 0
dry_run = True
if dry_run:
    n, k = 4, 2
    ids = [[4, 4, 6, 7, 8], [4, 8, 3, 0, 4], [2, 0, 10], [6, 1, 2, 3, 0, 5, 8]]
else:
    n, k = map(int, input().split())
    for i in range(n):
        ids.append([int(id) for id in input().split()])

print(ids)
