import sys

dry_run = True
if dry_run:
    input_file = open('absolute_min_max.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    pass
