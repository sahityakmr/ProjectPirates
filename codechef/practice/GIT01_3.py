t = int(input())
while t>0:
    n,m = map(int,input().split())
    a = []
    for r in range(n):
        a.append(list(input()))
    def calc(a,x):
        cost = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] != x:
                    if a[i][j] == 'G':
                        a[i][j] = 'R'
                        cost += 3
                    else:
                        a[i][j] = 'G'
                        cost += 5
                if x == 'R':
                    x = 'G'
                else:
                    x = 'R'
            if a[i][0] == 'R':
                x = 'G'
            else:
                x = 'R'
        return cost
    b = a.copy()
    print(a)
    a[0][0] = 'g'
    print(b)
    '''
    
    c1 = calc(a,'G')
    print(a)
    print(b)
    c2 = calc(b,'R')
    print(b)
    print(min(c1,c2))
    '''
    t -= 1