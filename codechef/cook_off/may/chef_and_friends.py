for t in range(int(input())):
    s = input()
    lens = len(s)
    if lens < 4:
        print(0)
        continue
    ways = 0
    for i in range(int((lens - 2) / 2)):
        l = i + 1
        i1 = 0
        i2 = l
        i3 = 2 * l
        i4 = i3 + int((lens - i3) / 2)
        i5 = lens
        # print(i1, i2, i3, i4, i5)
        if s[i1:i2] == s[i2:i3] and s[i3:i4] == s[i4:i5]:
            ways += 1
    print(ways)
