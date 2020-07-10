t = int(input())
while t>0:
    n = int(input())
    R = set()
    count = 0
    for i in input().split():
        a = int(i)
        if a not in R:
            count += 1
            R.add(a)
    print(n-count)
    t -= 1



