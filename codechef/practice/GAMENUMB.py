t = int(input())
while t>0:
    n, k = map(int,input().split())
    A = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    S = []

    D = [x for _, x in sorted(zip(A, D))]
    A = sorted(A)

    for i in range(n):
        S.extend([A[i]]*D[i])
    n = len(S)
    upperBound = n - 1
    lowerBound = 0
    for i in range(k):
        if i % 2 == 0:
            lowerBound = (upperBound-B[i]+1)
        else:
            upperBound = (lowerBound + B[i] - 1)
    S = S[lowerBound:upperBound+1]
    print(sum(S))
    t -= 1
