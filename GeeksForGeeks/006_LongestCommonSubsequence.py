# recursive approach
def lcs(x,y,m,n):
    if m==0 or n==0:
        return 0
    if x[m-1] == y[n-1]:
        return 1 + lcs(x,y,m-1,n-1)
    else:
        return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))

# tabulation approach
def lcsT(x,y):
    m = len(x)
    n = len(y)

    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j==0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])


s1 = "AGGTAB"
s2 = "GXTXAYB"
print(lcs(s1,s2,len(s1),len(s2)))