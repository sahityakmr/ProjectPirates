mod = 10 ** 9 + 7


def exp(base, exp):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp = int(exp / 2)
    return res % mod


for t in range(int(input())):
    s = str(input())
    value = 0
    l = len(s)
    for i in range(l):
        c = s[l - i - 1]
        if c not in ['a', 'e', 'i', 'o', 'u']:
            new = exp(2, i)
            value = value + new
            value = value % mod
    print(value % mod)