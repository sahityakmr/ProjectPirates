for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    prev = arr[0]
    map = dict()
    map[prev] = 1
    prepared = True
    for i in range(1, len(arr)):
        if arr[i] == prev:
            map[prev] += 1
        elif arr[i] not in map:
            prev = arr[i]
            map[prev] = 1
        else:
            prepared = False
            break

    ingred = set()
    if prepared:
        for key in map:
            if map[key] not in ingred:
                ingred.add(map[key])
            else:
                prepared = False
                break
    if prepared:
        print("YES")
    else:
        print("NO")