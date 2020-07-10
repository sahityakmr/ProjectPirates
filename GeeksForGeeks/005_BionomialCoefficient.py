#Naive Recursive Implementation
def biCoef(n,k):
    if k==0 or k==n:
        return 1
    return biCoef(n-1,k-1)+biCoef(n-1,k)

#storage based solution
def biCoeff(n,k):
    c = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]
    #print(c)
    return c[n][k]

print(biCoef(5,2))
print(biCoeff(5,2))