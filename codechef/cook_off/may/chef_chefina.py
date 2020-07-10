my_map = dict()
doubles = []
odds = []
n, m = -1, -1
d_i = 0
o_i = 0


def add(num):
    if num in my_map:
        my_map[num] += 1
    else:
        my_map[num] = 1


def make_matrix():
    global d_i, o_i
    for f in range(n):
        temp = [0] * m
        start, end = 0, m - 1
        while start < end:
            temp[start] = doubles[d_i]
            temp[end] = doubles[d_i + 1]
            d_i += 2
            start += 1
            end -= 1
        if start == end:
            if o_i < len(odds):
                temp[start] = odds[o_i]
                o_i += 1
            else:
                temp[start] = doubles[d_i]
                d_i += 1
        print(*temp, sep=' ')


for t in range(int(input())):
    n, m = map(int, input().split())
    odds.clear()
    doubles.clear()
    my_map.clear()
    d_i = 0
    o_i = 0
    for j in range(n):
        for i in input().split():
            add(int(i))

    for key in my_map:
        count = my_map[key]
        if count % 2 != 0:
            odds.append(key)
            count -= 1
        doubles.extend([key] * count)

    total_elem = n * m
    if m % 2 == 0:
        if len(doubles) == total_elem:
            make_matrix()
        else:
            print(-1)
    else:
        if len(doubles) >= (total_elem - n) and (len(doubles) - total_elem + n + len(odds)) == n:
            make_matrix()
        else:
            print(-1)
