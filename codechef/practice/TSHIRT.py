MAX_T_SHIRT = 100
t_shirts_elephant_map = []
dp = []


def find(mask, t_shirt_id):
    if mask == 0:
        return 1
    if t_shirt_id < 0:
        return 0
    if dp[mask][t_shirt_id] != -1:
        return dp[mask][t_shirt_id]
    ans = find(mask, t_shirt_id - 1)
    for e_id in t_shirts_elephant_map[t_shirt_id]:
        if mask & (1 << e_id) > 0:
            ans += find(mask ^ (1 << e_id), t_shirt_id - 1)
    ans %= 1000000007
    dp[mask][t_shirt_id] = ans
    return ans


for t in range(int(input())):
    elephant_count = int(input())
    t_shirts_elephant_map = [list() for i in range(MAX_T_SHIRT)]
    dp = [[-1 for i in range(MAX_T_SHIRT)] for i in range(1 << elephant_count)]
    for elephant_id in range(elephant_count):
        t_shirts = [int(x) for x in input().split()]
        for t_shirt in t_shirts:
            t_shirts_elephant_map[t_shirt - 1].append(elephant_id)
    print(find((1 << elephant_count) - 1, MAX_T_SHIRT - 1))
