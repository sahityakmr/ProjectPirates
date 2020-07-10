t = int(input())
while t>0:
    n,m,c = map(int,input().split())
    divisors = [1]
    k = c
    for i in range(2,k+1):
        if k % i == 0:
            divisors.append(i)
    k = len(divisors)
    i = 0
    pairs = []
    while i<k and divisors[i]<=n:
        j = 0
        while j<k and divisors[j]<=m :
            if divisors[i]*divisors[j] == c:
                pairs.append([divisors[i], divisors[j]])
            j += 1
        i += 1
    print(len(pairs))
    t -= 1