for t in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    hash_map = dict()
    for c in s:
        if hash_map.get(c) is None:
            hash_map[c] = 1
        else:
            hash_map[c] += 1
    for i in range(q):
        c = int(input())
        pending_queue = 0
        for key in hash_map:
            if hash_map[key] > c:
                pending_queue += hash_map[key] - c
        print(pending_queue)
