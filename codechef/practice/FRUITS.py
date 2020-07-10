t = int(input())
while t>0:
    n,m,k = map(int,input().split())
    if abs(n-m)<=k:
        print("0")
    else:
        print(abs(n-m)-k)
    t -= 1