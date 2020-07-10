import sys

dry_run = False
if dry_run:
    input_file = open('res/tom_and_jerry_game.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    ts = int(input())

    # when ts is odd
    if ts % 2 == 1:
        print(int((ts - 1) / 2))
        continue

    # when ts is even
    ways = int(ts / 2) - 1

    while ts % 2 == 0:
        ways = int(ways / 2)
        ts = int(ts / 2)
    print(ways)
