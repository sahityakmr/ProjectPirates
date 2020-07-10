dp = visited = component = []


def dfs(i, component_num):
    visited[i] = True
    component[i] = component_num
    for k in robot_access_list[i]:
        if not visited[int(k)]:
            dfs(k, component_num)


def get(ini, curr, mask):
    ans = dp[ini][curr][mask]
    if ans + 1 > 0:
        return ans
    if ini == curr and mask == 0:
        return 1
    if ini == curr:
        for i in range(vase_count):
            if (mask & (1 << i)) > 0:
                ans = max(ans, (1 + get(component[i], component[vase_position[i]], mask - (1 << i))))
    else:
        for tup in G[curr]:
            if (mask & (1 << tup[1])) > 0:
                ans = max(ans, get(ini, tup[0], mask - (1 << tup[1])))
    if ans == -1:
        ans = 0
    return ans


for t in range(int(input())):
    vase_count, robot_count = map(int, input().split())
    vase_position = [int(i) - 1 for i in input().split()]
    visited = [False] * vase_count
    component = [0] * vase_count
    robot_access_list = [list() for i in range(vase_count)]
    G = [list() for i in range(vase_count)]
    dp = [[[-1 for i in range(1 << vase_count)] for j in range(vase_count)] for k in range(vase_count)]

    for i in range(robot_count):
        x, y = map(int, input().split())
        robot_access_list[x - 1].append(y - 1)
        robot_access_list[y - 1].append(x - 1)

    c = 0
    for i in range(vase_count):
        if not visited[i]:
            dfs(i, c)
            c += 1

    for i in range(vase_count):
        G[component[i]].append((component[vase_position[i]], i))

    ans = 0
    for i in range(vase_count):
        ans = max(ans, get(component[i], component[vase_position[i]], (1 << vase_count) - 1 - (1 << i)))
    print(vase_count - ans)
