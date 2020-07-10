t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    rX,rY = map(int,input().split())
    seqLen = int(input())
    seq = list(input())
    x,y = 0,0
    for c in seq:
        if c == 'D':
            y -= 1
        elif c == 'U':
            y += 1
        elif c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        #print(x,y)
    print("Case ",i+1,": ",end=' ',sep='')
    if x<0 or x>m or y<0 or y>n:
        print("DANGER")
    elif x==rX and y == rY:
        print("REACHED")
    else:
        print("SOMEWHERE")