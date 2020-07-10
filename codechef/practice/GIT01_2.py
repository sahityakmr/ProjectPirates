t = int(input())
while t>0:
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(input()))

    def notInRange(i,j):
        if i<n and i>=0 and j<m and j>=0:
            return False
        else:
            return True

    def mutateX(a,i,j,x):
        if a[i][j] == x:
            return 0
        if a[i][j] == 'G':
            a[i][j] = 'R'
            return 3
        if a[i][j] == 'R':
            a[i][j] = 'G'
            return 5

    def calCost(a):
        for i in range(n-1):
            for j in range(m):
                j = 1




    #print(a)
    b = a
    #calCost(a, 0, 0, 'G')
    c1 = c
    #print(a)
    #print(b)
    c = 0
    #calCost(b, 0, 0, 'R')
    c2 = c
    #print(b)
    print(min(c1,c2))
    t -= 1