import sys
dry_run = True
if dry_run:
    input_file = open('convert_the_string.txt')
    sys.stdin = input_file

global initial_map, final_map, result
for t in range(int(input())):
    length = int(input())
    initial = input()
    final = input()
    initial_map = dict()
    final_map = dict()
    result = list()
    possible = True
    for index in range(length):
        if initial[index] in initial_map:
            initial_map[initial[index]].add(index)
        else:
            my_set = set()
            my_set.add(index)
            initial_map[initial[index]] = my_set

        if final[index] in final_map:
            final_map[final[index]].add(index)
        else:
            my_set = set()
            my_set.add(index)
            final_map[final[index]] = my_set

        if final[index] > initial[index]:
            possible = False
            break

    if possible:
        for key in final_map:
            if key not in initial_map:
                possible = False
                break

    if possible:
        final_keys = [key for key in final_map]
        final_keys = sorted(final_keys, reverse=True)
        for char in final_keys:
            if char in initial_map and len(initial_map[char]) > 0:
                if not final_map[char].issubset(initial_map[char]):
                    temp_set = set()
                    temp_set.update(final_map[char])
                    temp_set.update(initial_map[char])
                    result.append(temp_set)
                    for index in final_map[char]:
                        initial_map[initial[index]].remove(index)
            else:
                possible = False
                break

    if possible:
        print(len(result))
        for res in result:
            print(len(res), end=' ')
            print(" ".join(str(r) for r in res))
    else:
        print(-1)
