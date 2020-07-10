t = int(input())
while t>0:
    n,k,b = map(int,input().split())
    li = []
    A = [int(i) for i in input().split()]
    maxLength = 0
    len = 0
    for i in range(0,n-maxLength):
        if(A[i]*k+b <= A[i+1]):
            len += 1
    t -= 1