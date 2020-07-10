import sys

dry_run = True
if dry_run:
    file = open('res/input.txt')
    sys.stdin = file

global var
for t in range(int(input())):
    s, n = map(int, input().split())
    count = 0
    dom = n
    while s > 0:
        if dom > s:
            dom = s
        if dom != 1 and dom % 2 == 1:
            dom -= 1
        used = int(s / dom)
        s -= used * dom
        count += used
    print(count)
