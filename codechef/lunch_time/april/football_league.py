for t in range(int(input())):
    n, s = map(int, input().split())
    prices = [int(i) for i in input().split()]
    type = [int(i) for i in input().split()]
    defenders = []
    attackers = []
    for i in range(len(type)):
        if type[i] == 0:
            defenders.append(prices[i])
        else:
            attackers.append(prices[i])
    defenders.sort()
    attackers.sort()
    if len(defenders) > 0 and len(attackers) > 0:
        if s + defenders[0] + attackers[0] <= 100:
            print('yes')
        else:
            print('no')
    else:
        print('no')