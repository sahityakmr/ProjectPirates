import sys

dry_run = True
if dry_run:
    file = open('res/tuple_operation.txt')
    sys.stdin = file

global var
for t in range(int(input())):
    p, q, r = map(int, input().split())
    a, b, c = map(int, input().split())
    a_satisfied = b_satisfied = c_satisfied = False

    # direct check
    if a == p:
        a_satisfied = True
    if b == q:
        b_satisfied = True
    if c == r:
        c_satisfied = True
    if a_satisfied and b_satisfied and c_satisfied:
        print(0)
        continue

    # one addition check
    diff = list()
    if not a_satisfied and a - p != 0:
        diff.append(a - p)
    if not b_satisfied and b - q != 0:
        diff.append(b - q)
    if not c_satisfied and c - r != 0:
        diff.append(c - r)
    if min(diff) == max(diff):
        print(1)
        continue

    # one divide check
    div = list()
    if not a_satisfied:
        div.append(a / p)
    if not b_satisfied:
        div.append(b / q)
    if not c_satisfied:
        div.append(c / r)
    if min(div) == max(div) and div[0] == int(div[0]):
        print(1)
        continue
    pass

    # two op checks
    # two addition check
    diff = sorted(diff)
    if len(diff) == 2 or diff[0] == diff[1] or diff[1] == diff[2]:
        print(2)
        continue

    # two multiplication check
    div = sorted(div)
    if (len(div) == 2 and int(div[0]) == div[0] and int(div[1]) == div[1]) \
            or (div[0] == div[1] and int(div[0]) == div[0]) \
            or (div[1] == div[2] and int(div[1]) == div[1]):
        print(2)
        continue

    # multiplication followed by addition

    # addition followed by multiplication

    print(3)
