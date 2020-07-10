t = int(input())
while t > 0:
    c, d, l = map(int, input().split())
    maxLegs = (c + d) * 4
    minLegs = d * 4
    if c > 2 * d:
        minLegs = (d + (c - 2 * d)) * 4
    if (l > maxLegs or l < minLegs):
        print("no")
    else:
        leftLegs = l - d * 4
        if leftLegs % 4 == 0:
            print("yes")
        else:
            print("no")
    t = t - 1
