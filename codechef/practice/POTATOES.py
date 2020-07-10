def generatePrime(n):
    while True:
        n = n + 1
        if isPrime(n) == True:
            return n


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    x = int(n ** (0.5))
    for i in range(2, x+1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    x, y = map(int, input().split())
    print(generatePrime(x+y)-(x+y))
    t = t - 1
