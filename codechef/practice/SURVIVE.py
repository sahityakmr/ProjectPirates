import math
t = int(input())
while t>0:
    n,k,s = map(int,input().split())
    if (int(n/k)==1 and s>1) or int(n/k)<1:
        print(-1)
    else:
        print(math.ceil(s/int(n/k)))
    t -= 1