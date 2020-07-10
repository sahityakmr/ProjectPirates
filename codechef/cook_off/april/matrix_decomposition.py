def fast_exp_rec(base, exp):
    if exp == 1:
        return base
    if exp % 2 == 0:
        ans = fast_exp_rec(base, exp / 2) ** 2
    else:
        ans = base * fast_exp_rec(base, (exp - 1) / 2) ** 2
    if ans > mod:
        ans %= mod
    return ans


def fast_exp(base, exp):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp = int(exp / 2)
    return res % mod


for t in range(int(input())):
    n, a = map(int, input().split())
    s_prod = 0
    mod = 1000000007
    for i in range(n):
        prod = fast_exp(a, (2 * i + 1))
        a = (a * prod) % mod
        s_prod = (s_prod + prod) % mod
    print(s_prod)
