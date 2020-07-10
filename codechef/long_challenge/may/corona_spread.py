for t in range(int(input())):
    n = int(input())
    dist = [int(i) for i in input().split()]

    infections = []
    for i in range(n):
        back_infections = 0
        k = i
        while k > 0 and abs(dist[k - 1] - dist[k]) <= 2:
            back_infections += 1
            k -= 1
        forward_infections = 0
        k = i
        while k < n - 1 and abs(dist[k + 1] - dist[k]) <= 2:
            back_infections += 1
            k += 1
        total_infections = back_infections + forward_infections + 1
        infections.append(total_infections)
        # print('i : %d, back_infections : %d, forward_infections : %d' % (i, back_infections, forward_infections))

    print(min(infections), max(infections))