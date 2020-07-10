mod = 10**9 + 7
cats = []


def cat(n):
    if n == 0 or n == 1:
        return 1
    cats[0] = 1
    cats[1] = 1
    for i in range(2, n + 1):
        cats[i] = 0
        for j in range(i):
            cats[i] = (cats[i] + ((cats[j] * cats[i - j - 1]) % mod) % mod)
    return cats[n]


for t in range(int(input())):
    stri = input()
    cats = [0] * len(stri)
    print(cat(len(stri) - 1))
