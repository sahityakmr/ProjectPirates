import sys

dry_run = True
if dry_run:
    file = open('res/tuple_operation.txt')
    sys.stdin = file

global new_init, new_final


def case_zero():
    # first op on all followed by second op on all

    # multiply then add
    div = list()
    mod = list()
    for i in range(len(new_init)):
        div.append(int(new_final[i] / new_init[i]))
        mod.append(new_final[i] % new_init[i])

    if min(div) == max(div) and min(mod) == max(div):
        return True
    return False


def case_one():
    # first op on two followed by second op on 1 new and one prev
    return False


def case_two():
    # first op on two and second on all, and vice versa
    return False


for t in range(int(input())):
    initial = [int(i) for i in input().split()]
    final = [int(i) for i in input().split()]

    # pre-processing
    new_init = list()
    new_final = list()
    for i in range(3):
        if initial[i] != final[i]:
            new_init.append(initial[i])
            new_final.append(final[i])

    if len(new_init) == 0:
        print(0)
        continue

    # one addition check
    diff = list()
    for i in range(len(new_init)):
        diff.append(new_final[i] - new_init[i])
    if min(diff) == max(diff):
        print(1)
        continue

    # one divide check
    div = list()
    for i in range(len(new_init)):
        div.append(new_final[i] / new_init[i])
    if min(div) == max(div) and div[0] == int(div[0]):
        print(1)
        continue

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

    if case_zero() or case_one() or case_two():
        print(2)
        continue

    print(3)
