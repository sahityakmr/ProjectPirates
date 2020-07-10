import math

for t in range(int(input())):
    n, k = map(int, input().split())
    seq = [int(i) for i in input().split()]
    r = int(math.ceil(n / k))
    mat = [[0] * k] * r
    i = 0
    for col in range(k - 1):
        for row in range(r):
            mat[row][col] = seq[i]
            i += 1

    print(mat)


# 1
# 8 3
# 2 3 5 7 1 6 9 2
