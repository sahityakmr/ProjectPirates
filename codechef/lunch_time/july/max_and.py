import sys

dry_run = True
if dry_run:
    file = open('res/input_max.txt')
    sys.stdin = file

global var
for t in range(int(input())):
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]

    pass
