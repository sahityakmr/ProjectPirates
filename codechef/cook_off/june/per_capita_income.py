import sys

dry_run = True
if dry_run:
    file = open('res/per_income.txt')
    sys.stdin = file


def take_first(val):
    return val[0]


global var
for t in range(int(input())):
    cities, roads = map(int, input().split())
    incomes = [int(i) for i in input().split()]
    population = [int(i) for i in input().split()]
    ratio = list()
    for i in range(cities):
        ratio.append([incomes[i] / population[i], i])
    ratio = sorted(ratio, key=take_first, reverse=True)

    chosen_state = set()
    rat = ratio[0][0]
    i = 0
    while i < cities and ratio[i][0] == rat:
        chosen_state.add(ratio[i][1])
        i += 1
    my_dict = dict()
    for state in chosen_state:
        ms = list()
        ms.append(state)
        my_dict[state] = ms
    max = 1
    max_set = None
    for road in range(roads):
        s, d = map(int, input().split())
        s -= 1
        d -= 1
        if s in chosen_state and d in chosen_state:
            my_dict[s].append(d)
            my_dict[d].append(s)
            if len(my_dict[s]) > max:
                max = len(my_dict[s])
                max_set = my_dict[s]
            if len(my_dict[d]) > max:
                max = len(my_dict[d])
                max_set = my_dict[d]
    if max == 1:
        print(1)
        print(chosen_state.pop() + 1)
    else:
        print(len(max_set))
        print(" ".join(str(int(s) + 1) for s in max_set))
    pass
