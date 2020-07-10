import sys

dry_run = True
if dry_run:
    input_file = open('escape_one.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    pass
