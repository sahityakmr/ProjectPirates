t = int(input())
lead = 0
win = 0
x,y = 0,0
while t>0:
    a,b = map(int,input().split())
    x+=a
    y+=b
    diff = abs(x-y)
    #print(x,y,diff)
    if diff>lead:
        lead = diff
        if a>b:
            win = 1
        else:
            win = 2
    t -= 1
print(win,lead)