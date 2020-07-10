import math
t = int(input())
while t>0:
    n,h = map(int,input().split())
    stack = [int(i) for i in input().split()]
    if n==h:
        print(max(stack))
    else:
        sm = sum(stack)/h
        if sm == int(sm):
            num = sm + 1
        else:
            num = math.ceil(sm)
        num = int(num)
        #print(num)
        possibleSpeeds = [num, num + 1, num + 2, num + 3, num + 4, num + 5, num + 6]
        #print(possibleSpeeds)
        correspondingRequiredHrs = [0] * 7
        #print(correspondingRequiredHrs)
        for i in stack:
            correspondingRequiredHrs[0] += math.ceil(i / possibleSpeeds[0])
            correspondingRequiredHrs[1] += math.ceil(i / possibleSpeeds[1])
            correspondingRequiredHrs[2] += math.ceil(i / possibleSpeeds[2])
            correspondingRequiredHrs[3] += math.ceil(i / possibleSpeeds[3])
            correspondingRequiredHrs[4] += math.ceil(i / possibleSpeeds[4])
            correspondingRequiredHrs[5] += math.ceil(i / possibleSpeeds[5])
            correspondingRequiredHrs[6] += math.ceil(i / possibleSpeeds[6])
        k=0
        #print(correspondingRequiredHrs)
        for i in correspondingRequiredHrs:
            if i == h:
                print(possibleSpeeds[k])
                break
            k += 1
    t -= 1