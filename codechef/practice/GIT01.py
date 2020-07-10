t = int(input())
while t>0:
    n,m = map(int,input().split())
    G2R = 3
    R2G = 5

    def inv(s):
        if s == 'G':
            return 'R'
        else:
            return 'G'
    c=0
    def inRange(i,j):
        if i<n and i>=0 and j<m and j>=0:
            return True
        else:
            return False

    def calCost(a,i,j,s):
        global c
        if inRange(i,j) == False:
            #print("returning",i,j)
            return c

        if a[i][j] == s:
            calCost(a,i+1,j,inv(s))
            calCost(a,i,j+1,inv(s))
        else:
            a[i][j] = inv(s)
            if s=='G':
                c += G2R
            else:
                c += R2G
            calCost(a, i + 1, j, inv(s))
            calCost(a, i, j + 1, inv(s))

    a = []
    for i in range(n):
        a.append(list(input()))
    #print(a)
    b = a
    calCost(a, 0, 0, 'G')
    c1 = c
    #print(a)
    #print(b)
    c = 0
    calCost(b, 0, 0, 'R')
    c2 = c
    #print(b)
    print(min(c1,c2))
    t -= 1