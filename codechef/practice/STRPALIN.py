t = int(input())
while t>0:
    str1 = str(input())
    str2 = str(input())
    flag = False
    for c in str1:
        if c in str2:
            flag = True
            break
    if(flag):
        print("Yes")
    else:
        print("No")
    t -= 1