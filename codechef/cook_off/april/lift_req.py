for t in range(int(input())):
    n, q = map(int, input().split())
    sum = 0
    l = 0
    for i in range(q):
        s, d = map(int, input().split())
        sum += abs(l - s) + abs(d - s)
        l = d
    print(sum)