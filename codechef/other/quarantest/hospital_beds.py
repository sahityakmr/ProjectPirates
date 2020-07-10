x_dis = [-1, 0, 1, 0]
y_dis = [0, -1, 0, 1]
for t in range(int(input())):
    n = int(input())
    bed_pos = []
    for i in range(n):
        bed_pos.append([int(k) for k in input().split()])
    violation = False
    for i in range(n):
        for j in range(n):
            for k in range(4):
                x = i + x_dis[k]
                y = j + y_dis[k]
            if bed_pos[i][j] == 1 and 0 <= x < n and 0 <= y < n and bed_pos[x][y] == 1:
                violation = True
                break
            if violation:
                break
    if violation:
        print('UNSAFE')
    else:
        print('SAFE')