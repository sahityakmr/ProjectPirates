def get_indices():
    global is_sorted
    if len(unsorted_indices) <= 0:
        if len(unsorted_swapped_tuples) % 2 != 0:
            return -1, -1, -1
        if len(unsorted_swapped_tuples) > 1:
            tup1 = unsorted_swapped_tuples.pop()
            tup2 = unsorted_swapped_tuples.pop()
            unsorted_indices.add(tup1[0])
            unsorted_indices.add(tup1[1])
            unsorted_indices.add(tup2[0])
            unsorted_indices.add(tup2[1])
            return tup1[0], tup2[0], tup1[1]
        is_sorted = True
        return -1, -1, -1
    i1 = unsorted_indices.pop()
    i3 = index_of[i1 + 1]
    i2 = index_of[i3 + 1]

    if i1 == i2 or i2 == i3 or i1 == i3:
        unsorted_swapped_tuples.add((i1, i3))
        unsorted_indices.remove(i3)
        return get_indices()
    unsorted_indices.add(i1)
    return i1, i2, i3


for t in range(int(input())):
    n, k = map(int, input().split())
    array = [int(i) for i in input().split()]
    o_array = list(array)
    index_of = [-1] * (n + 1)
    unsorted_indices = set()
    unsorted_swapped_tuples = set()
    is_sorted = False
    for i in range(n):
        if array[i] != i + 1:
            unsorted_indices.add(i)
        index_of[array[i]] = i

    iterations = 0
    steps = str()
    while len(unsorted_indices) > 0 or len(unsorted_swapped_tuples) > 0:
        i1, i2, i3 = get_indices()
        if i1 == -1:
            break
        temp = array[i1]
        array[i1] = array[i3]
        array[i3] = array[i2]
        array[i2] = temp

        for index in [i1, i2, i3]:
            if array[index] == index + 1:
                unsorted_indices.remove(index)
            else:
                index_of[array[index]] = index

        iterations += 1
        steps += "{} {} {}\n".format(i1 + 1, i2 + 1, i3 + 1)

    if len(unsorted_indices) == 0 and len(unsorted_swapped_tuples) == 0 and iterations <= k:
        print(iterations)
        print(steps)
    else:
        print(-1)
