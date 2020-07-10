t = int(input())
while t>0:
    n = int(input())
    B = [int(i) for i in input().split()]
    s = sum(B)
    if s >= 100:
        if s==100:
            print("YES")
        elif (s-100)<len(B):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1