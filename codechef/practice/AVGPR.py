t = int(input())
while t>0:
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2 == 0 and (a[i]+a[j])/2 in a:
                count += 1
    print(count)
    t -= 1