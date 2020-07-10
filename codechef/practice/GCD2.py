# GCD function
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

# main execution
t = int(input())
while t > 0:
    a, b = map(int, input().split())
    c = gcd(a, b)
    print(c)
    t = t - 1
