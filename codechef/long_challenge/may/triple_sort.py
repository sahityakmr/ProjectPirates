dry_run = True
T = 5
_n = [7, 9, 9, 9, 9]
_k = [3, 5, 5, 5, 5]
_array = [
    [2, 1, 3, 7, 5, 6, 4],
    [1, 9, 8, 6, 7, 4, 2, 5, 3],
    [2, 9, 5, 6, 1, 8, 3, 7, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 8, 7, 6, 5, 4, 3, 2, 9]
]
if not dry_run:
    T = int(input())


def not_possible():
    for key in original_to_sorted:
        # check if we have (o2s[key], key)
        val = original_to_sorted[key]
        if original_to_sorted[val + 1] == key - 1:
            return True
    return False


def check(array, step_list):
    sorted_array = sorted(array)
    for [i1, i2, i3] in step_list:
        temp = array[i1]
        array[i1] = array[i3]
        array[i3] = array[i2]
        array[i2] = temp
    for i in range(len(array)):
        if array[i] != sorted_array[i]:
            print('----------Test Failed------------')
            return
    print('verified')


for t in range(T):
    res = []

    n = _n[t]
    k = _k[t]
    array = _array[t]
    if not dry_run:
        n, k = map(int, input().split())
        array = [int(i) for i in input().split()]
    o_array = list(array)
    original_to_sorted = dict()
    unsorted_values = set()
    for i in range(n):
        if array[i] != i + 1:
            original_to_sorted[array[i]] = i
            unsorted_values.add(array[i])

    if dry_run:
        print(original_to_sorted)
        print(unsorted_values)

    if not_possible():
        print(-1)
        continue

    iterations = 0
    steps = str()
    step_list = list()
    while len(unsorted_values) >= 3:
        value = next(iter(unsorted_values))
        i1 = original_to_sorted[value]  # current index of the value
        i2 = value - 1  # correct index of the value
        i3 = array[i2] - 1  # correct index of correct index of the value
        temp = array[i1]

        array[i1] = array[i3]
        array[i3] = array[i2]
        array[i2] = temp

        unsorted_values.remove(array[i2])
        unsorted_values.remove(array[i3])

        original_to_sorted.pop(array[i2])
        original_to_sorted.pop(array[i3])

        original_to_sorted[array[i1]] = i1

        if array[i1] == i1 + 1:
            unsorted_values.remove(array[i1])
            original_to_sorted.pop(array[i1])

        iterations += 1
        steps += "{} {} {}\n".format(i1 + 1, i2 + 1, i3 + 1)
        step_list.append([i1, i2, i3])
        if dry_run and False:
            print('Iteration', iterations)
            print(i1, i2, i3)
            print(original_to_sorted)
            print(unsorted_values)

    if dry_run:
        check(o_array, step_list)

    if iterations <= k:
        print(iterations)
        print(steps)
    else:
        print(-1)
