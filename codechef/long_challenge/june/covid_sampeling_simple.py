import sys

dry_run = True
if dry_run:
    file = open('res/covid_sampling.txt')
    sys.stdin = file

global mat


for t in range(int(input())):
    n, p = map(int, input().split())
    mat = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(1, i, j, i, j)
            mat[i][j] = int(input())
    print(2)
    mat = mat[1:]
    for _row in mat:
        print(" ".join(str(r) for r in _row[1:]))
    x = int(input())
    if x == -1:
        break
    pass
