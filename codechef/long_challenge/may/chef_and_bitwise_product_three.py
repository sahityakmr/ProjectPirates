dry_run = True
inputs = [
    [10, 45, 0, 10],
    [35, 69, 15, 24],
    [8, 45, 28, 40],
    [34, 70, 14, 25],
    [12, 51, 2, 34],
    [37, 75, 17, 48],
    [11, 53, 1, 35],
    [36, 77, 16, 49],
    [14, 40, 4, 41],
    [39, 64, 19, 55],
    [13, 41, 3, 42],
    [38, 65, 18, 56],
    [16, 47, 6, 29],
    [42, 72, 22, 44],
    [15, 48, 5, 31],
    [41, 73, 21, 46],
    [1, 4, 21, 49],
    [26, 28, 6, 33],
    [0, 5, 20, 50],
    [25, 29, 5, 34],
    [3, 10, 23, 23],
    [28, 34, 8, 57],
    [2, 11, 22, 24],
    [27, 35, 7, 8],
    [5, 49, 25, 29],
    [31, 74, 11, 14],
    [4, 50, 24, 30],
    [30, 75, 10, 15],
    [7, 55, 27, 68],
    [33, 80, 13, 53],
    [6, 6, 26, 69],
    [32, 81, 12, 54],
    [27, 47, 17, 62],
    [3, 22, 3, 47],
    [26, 48, 16, 64],
    [2, 23, 2, 49],
    [29, 54, 19, 36],
    [5, 29, 5, 21],
    [28, 55, 18, 38],
    [4, 30, 4, 23],
    [32, 43, 22, 44],
    [7, 17, 7, 28],
    [30, 44, 20, 44],
    [6, 19, 6, 29],
    [34, 50, 24, 33],
    [9, 24, 9, 17],
    [33, 51, 23, 34],
    [8, 25, 8, 18],
    [18, 56, 8, 21],
    [44, 81, 24, 36],
    [17, 57, 7, 22],
    [43, 82, 23, 37],
    [21, 63, 11, 55],
    [46, 87, 26, 69],
    [19, 63, 9, 55],
    [45, 88, 25, 70],
    [23, 52, 13, 62],
    [48, 76, 28, 76],
    [22, 53, 12, 13],
    [47, 77, 27, 27],
    [25, 58, 15, 50],
    [0, 32, 0, 34],
    [24, 60, 14, 52],
    [49, 84, 29, 66],
    [45, 60, 5, 45],
    [20, 34, 20, 59],
    [44, 61, 4, 46],
    [19, 35, 19, 60],
    [47, 66, 7, 19],
    [22, 40, 22, 33],
    [46, 67, 6, 20],
    [21, 41, 21, 34],
    [49, 55, 9, 25],
    [25, 30, 25, 40],
    [48, 56, 8, 26],
    [24, 31, 24, 41],
    [1, 11, 11, 14],
    [27, 36, 27, 29],
    [0, 12, 10, 15],
    [26, 37, 26, 30],
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
    or_z = x | y
    and_z = x & y

    if r > or_z:
        return or_z
    if l > or_z or x == 0 or y == 0:
        return 0

    bin_or_z = bin(or_z)
    bin_and_z = bin(and_z)

    max_val = r
    powers = set()

    pow = len(bin_and_z) - 2
    for i in range(2, len(bin_and_z)):
        pow -= 1
        if int(bin_and_z[i]) == 1 and pow not in powers and max_val >= 2 ** pow:
            powers.add(pow)
            max_val -= 2 ** pow

    pow = len(bin_or_z) - 2
    for i in range(2, len(bin_or_z)):
        pow -= 1
        if int(bin_or_z[i]) == 1 and pow not in powers and max_val >= 2 ** pow:
            powers.add(pow)
            max_val -= 2 ** pow

    ans1 = 0
    for s in powers:
        ans1 += 2 ** s

    powers = set()
    max_val = r
    pow = len(bin_or_z) - 2
    for i in range(2, len(bin_or_z)):
        pow -= 1
        if int(bin_or_z[i]) == 1 and max_val >= 2 ** pow:
            powers.add(pow)
            max_val -= 2 ** pow

    ans2 = 0
    for s in powers:
        ans2 += 2 ** s

    if (x & ans2) * (y & ans2) > (x & ans1) * (y & ans1):
        return ans2
    return ans1


for t in range(T):
    x = y = l = r = 0
    if dry_run:
        x, y, l, r = inputs[t]
    else:
        x, y, l, r = map(int, input().split())
    my = get_z(x, y, l, r)
    if dry_run:
        correct = get_max(x, y, l, r)
        if my == correct:
            # print('verified')
            pass
        elif my >= l:
            print('not-verified     | x : {}, y : {}, l : {}, r : {}, calculated : {}, correct : {}'
                  .format(x, y, l, r, my, correct))
            print('bin(x) :', bin(x), '\tbin(y) :', bin(y), '\tbin(correct) :', bin(correct), '\tbin(calculated) :',
                  bin(my), '\n')
    else:
        print(my)
