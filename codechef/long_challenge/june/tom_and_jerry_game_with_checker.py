import sys

dry_run = True
if dry_run:
    input_file = open('res/tom_and_jerry_game.txt')
    sys.stdin = input_file


def play(jerry, tom):
    if jerry & 1 == 0:
        if tom & 1 == 0:
            return play(jerry >> 1, tom >> 1)
        else:
            return 1
    else:
        return 0


global var
for t in range(int(input())):
    ts = int(input())

    orts = ts

    # when ts is odd
    if ts & 1 == 1:
        won = 0
        for j in range(1, ts + 1):
            won += play(j, orts)
        print(int((ts - 1) / 2), won)
        continue

    # when ts is even
    ways = int(ts / 2) - 1

    while ts & 1 == 0:
        ways = ways >> 1
        ts = ts >> 1

    won = 0
    for j in range(1, orts + 1):
        won += play(j, orts)

    print(ways, won)
