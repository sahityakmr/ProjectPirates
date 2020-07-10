import sys

dry_run = True
if dry_run:
    file = open('res/input.txt')
    sys.stdin = file

global var
for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    preset = set()
    posset = set()
    np = False
    for i in arr:
        if i in posset:
            np = True
            break
        if i in preset:
            posset.add(i)
        else:
            preset.add(i)
    if np or (len(posset) != 0 and max(preset) == max(posset)):
        print("NO")
    else:
        poslist = list(posset)
        print("YES")
        for i in preset:
            print(i, end=' ')
        for i in reversed(poslist):
            print(i, end=' ')
        print()

