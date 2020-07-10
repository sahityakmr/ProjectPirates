from collections import deque
x_dis = [-1, 0, 1, 0]
y_dis = [0, -1, 0, 1]
for t in range(int(input())):
    row, col = map(int, input().split())
    r, c = map(int, input().split())
    state = [[0 for i in range(col)] for j in range(row)]
    infected = deque()
    infected.append((r, c))
    state[r][c] = 1
    days = 0
    while len(infected) > 0:
        # print('day :', days)
        # print(*state, sep="\n")
        new_cases = deque()
        days += 1
        while len(infected) > 0:
            pos = infected.popleft()
            for k in range(4):
                r = pos[0] + y_dis[k]
                c = pos[1] + x_dis[k]
                if 0 <= c < col and 0 <= r < row and state[r][c] == 0:
                    new_cases.append((r, c))
                    state[r][c] = 1
        infected = new_cases
    # print('day :', days)
    # print(*state, sep="\n")
    print(days - 1)

