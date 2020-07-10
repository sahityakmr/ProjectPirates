t = int(input())
while t>0:
    n = int(input())
    sm = 0
    while n>0:
        sm += n%10
        n = int(n/10)
    print(sm)
    t -= 1