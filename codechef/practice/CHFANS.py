def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

t = int(input())
while t > 0:
    s1, s2 = map(int, input().split())
    print(int(abs(s1-s2)/gcd(abs(s1), abs(s2))))
    t = t - 1
