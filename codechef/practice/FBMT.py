t = int(input())
while t>0:
    n = int(input())
    if n == 0:
        print("Draw")
        t -= 1
        continue
    cs = 0
    cp = 0
    s = input()
    cs += 1
    p = None
    while n>1:
        x = input()
        if x == s:
            cs += 1
        else:
            p = x
            cp += 1
        n -= 1
    if cs>cp:
        print(s)
    elif cs<cp:
        print(p)
    else:
        print("Draw")
    t -= 1