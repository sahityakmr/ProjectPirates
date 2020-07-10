import sys

dry_run = True
if dry_run:
    input_file = open('res/chef_and_icecream.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    coin_map = dict()
    coin_map[5] = 0
    coin_map[10] = 0
    coin_map[15] = 0
    success = True
    for val in a:
        if val == 5:
            coin_map[5] += 1
        if val == 10:
            if coin_map[5] > 0:
                coin_map[5] -= 1
                coin_map[10] += 1
            else:
                success = False
                break
        if val == 15:
            if coin_map[10] > 0:
                coin_map[10] -= 1
                coin_map[15] += 1
            elif coin_map[5] > 1:
                coin_map[5] -= 2
                coin_map[10] += 1
            else:
                success = False
                break
    if success:
        print("YES")
    else:
        print("NO")
    pass
