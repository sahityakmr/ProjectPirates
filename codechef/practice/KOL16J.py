t = int(input())
while t>0:
    n = int(input())
    A = [int(i) for i in input().split()]
    B = sorted(A)
    if B == A:
        print("no")
        t -= 1
        continue
    flag = False
    for i in range(1,n+1):
        if i not in A:
            flag = True
            break
    if flag:
        print("no")
    else:
        print("yes")
    t -= 1