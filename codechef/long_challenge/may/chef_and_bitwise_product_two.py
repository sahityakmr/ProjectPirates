dry_run = True
inputs = [
    [7, 12, 4, 17],
    [7, 12, 0, 8],
    [10, 45, 0, 20],
    [35, 69, 15, 44],
    [8, 45, 28, 20],
    [34, 70, 14, 45],
    [12, 51, 2, 44],
    [37, 75, 17, 68],
    [11, 53, 1, 45],
    [36, 77, 16, 69],
    [14, 40, 4, 51],
    [39, 64, 19, 75],
    [13, 41, 3, 52],
    [38, 65, 18, 76],
    [16, 47, 6, 39],
    [42, 72, 22, 64],
    [15, 48, 5, 41],
    [41, 73, 21, 66],
    [1, 4, 21, 29],
    [26, 28, 6, 53],
    [0, 5, 20, 30],
    [25, 29, 5, 54],
    [3, 10, 23, 3],
    [28, 34, 8, 77],
    [2, 11, 22, 4],
    [27, 35, 7, 28],
    [5, 49, 25, 9],
    [31, 74, 11, 34],
    [4, 50, 24, 10],
    [30, 75, 10, 35],
    [7, 55, 27, 48],
    [33, 80, 13, 73],
    [6, 6, 26, 49],
    [32, 81, 12, 74],
    [27, 47, 17, 72],
    [3, 22, 3, 47],
    [26, 48, 16, 74],
    [2, 23, 2, 49],
    [29, 54, 19, 46],
    [5, 29, 5, 21],
    [28, 55, 18, 48],
    [4, 30, 4, 23],
]
T = len(inputs)
if not dry_run:
    T = int(input())


def get_max(x, y, l, r):
    maxv = 0
    maxi = 0
    for i in range(l, r + 1):
        nmax = (x & i) * (y & i)
        if nmax > maxv:
            maxv = nmax
            maxi = i
    return maxi


def get_max_z(x, y, l, r, powers, sum, index):
    if sum > r:
        return 0
    if index == len(powers):
        if sum < l:
            return 0
        return sum
    p = get_max_z(x, y, l, r, powers, sum + 2 ** powers[index], index + 1)
    q = get_max_z(x, y, l, r, powers, sum, index + 1)
    ap = (p & x) * (p & y)
    aq = (q & x) * (q & y)
    # print(index, p, q, ap, aq)
    if ap == aq:
        return min(p, q)
    if ap < aq:
        return q
    return p


def get_z(x, y, l, r):
    exp_z = x | y
    if r > exp_z:
        if x == 0 or y == 0:
            return 0
        return exp_z
    if l > exp_z:
        return 0
    output = bin(exp_z)
    output_r = bin(r)
    powers = []
    powers_r = []
    p = 0
    for i in range(len(output) - 1, 1, -1):
        if int(output[i]) == 1:
            powers.append(p)
        p += 1
    p = 0
    for i in range(len(output_r) - 1, 1, -1):
        if int(output_r[i]) == 1:
            powers_r.append(p)
        p += 1
    a, b = l, r
    if len(powers) > 2:
        a = max(l, int(2 ** powers_r[-1] / 2))
        b = max(r, 2 ** powers_r[-1])
    # print('a and b', a, b, powers_r)
    return get_max(x, y, a, b) & exp_z


for t in range(T):
    x = y = l = r = 0
    if dry_run:
        x, y, l, r = inputs[t]
    else:
        x, y, l, r = map(int, input().split())
    my = get_z(x, y, l, r)
    print(my)
    if dry_run:
        correct = get_max(x, y, l, r)
        if my == correct:
            print('verified')
        else:
            print('not-verified', x, y, l, r, my, correct)
        print(bin(x), bin(y), bin(get_max(x, y, l, r)), l, r)
