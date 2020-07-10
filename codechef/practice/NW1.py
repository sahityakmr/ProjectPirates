t = int(input())
while t>0:
    n, day = map(str,input().split())
    n = int(n)
    k = n%7
    days = [4]*7
    dayMap = {
        'mon':0,
        'tues':1,
        'wed':2,
        'thurs':3,
        'fri':4,
        'sat':5,
        'sun': 6
    }
    i = dayMap.get(day)
    while k>0:
        days[i] += 1
        i = (i+1)%7
        k -= 1

    for d in days:
        print(d, end=' ')
    t -= 1