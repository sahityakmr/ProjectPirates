t = int(input())
while t>0:
    n,u,d = map(int,input().split())
    heights = [int(i) for i in input().split()]
    parachute = True
    position = 1
    for i in range(n-1):
        if heights[i+1]==heights[i]:
            position +=1
        elif heights[i+1]>heights[i] and (heights[i+1]-heights[i])<=u:
            position += 1
        elif heights[i+1]<heights[i]:
            if (heights[i]-heights[i+1])<=d:
                position += 1
            elif parachute:
                position += 1
                parachute = False
            else:
                break
        else:
            break
    print(position)
    t -= 1