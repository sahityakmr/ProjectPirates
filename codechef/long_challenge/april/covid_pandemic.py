for i in range(int(input())):
    n = input()
    a = [int(x) for x in input().split()]
    dist = 100
    res = 'YES'
    for v in a:
        if v == 1:
            if dist < 5:
                res = 'NO'
                break
            dist = 0
        else:
            dist += 1
    print(res)


