import sys

dry_run = True
if dry_run:
    input_file = open('res/even_matrix.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    n = int(input())

    if n % 2 != 0:
        for i in range(n):
            for j in range(1, n + 1):
                print(i * n + j, end=' ')
            print()
    else:
        toggle = True
        for i in range(n):
            if toggle:
                for j in range(1, n + 1):
                    print(i * n + j, end=' ')
                toggle = False
            else:
                for j in range(n, 0, -1):
                    print(i * n + j, end=' ')
                toggle = True
            print()
    pass
