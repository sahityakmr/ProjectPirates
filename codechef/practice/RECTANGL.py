t = int(input())
while t>0:
    A = sorted([int(i) for i in input().split()])
    if A[0]==A[1] and A[2]==A[3]:
        print("YES")
    else:
        print("NO")
    t -= 1