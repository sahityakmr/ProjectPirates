for t in range(int(input())):
    n = int(input())
    p = [int(k) for k in input().split()]
    p = sorted(p, reverse=True)
    profit = 0
    for i in range(n):
        if p[i] - i > 0:
            profit += p[i] - i
        profit = profit % 1000000007
    print(profit)