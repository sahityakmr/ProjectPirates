t = int(input())
while t>0:
    n = int(input())
    k = 1
    for i in range(1,n+1):
        k *= i
    print(k)
    t -= 1