t  = int(input())
while t>0:
    n = int(input())
    L = [int(i) for i in input().split()]
    G = [int(i) for i in input().split()]
    front = True
    back = True
    for i in range(n):
        if L[i]>G[i]:
            front = False
        if L[i]>G[n-i-1]:
            back = False
        if front == False and back == False:
            break
    if front and back:
        print("both")
    elif not front and not back:
        print("none")
    elif front:
        print("front")
    elif back:
        print("back")
    t -= 1