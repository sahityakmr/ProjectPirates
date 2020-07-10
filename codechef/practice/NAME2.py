def subSeq(str1, str2):
    j = i = 0
    while True:
        while str2[j] != str1[i]:
            j = j + 1
            if j >= len(str2):
                return False
        i = i + 1
        if i >= len(str1):
            return True

t = int(input())
while t > 0:
    str1, str2 = map(list, input().split())
    if len(str1) > len(str2):
        c = subSeq(str2, str1)
    else:
        c = subSeq(str1, str2)
    if c:
        print("YES")
    else:
        print("NO")
    t = t - 1
