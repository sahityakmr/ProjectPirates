n,k = map(int,input().split())
c = 0
while n > 0:
    x = int(input())
    if x % k == 0:
        c += 1
    n -= 1
print(c)
