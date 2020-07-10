MIN_VAL = -10000000001
dry_run = True
if dry_run:
    # n, k = 5, 2
    # values = [5, 3, -2, 1, 1]

    # n, k = 2, 2
    # values = [5, 3]

    n, k = 10, 6
    values = [900, -300, -200, -500, -400, -300, -200, -200, -200, -500]

    # n, k = 10, 2
    # values = [-5, -3, -2, -1, -1, -2, -2, -2, -2, -50]
else:
    n, k = map(int, input().split())
    values = [int(i) for i in input().split()]

backward = [MIN_VAL] * n
forward = [MIN_VAL] * n
k -= 1

backward[0] = values[0]
for i in range(n - 2):
    backward[i + 1] = max(backward[i + 1], backward[i] + values[i + 1])
    backward[i + 2] = max(backward[i + 2], backward[i] + values[i + 2])
if n > 1:
    backward[n - 1] = max(backward[n - 1], backward[n - 2] + values[n - 1])

forward[k] = values[k]
for i in range(k, n - 2):
    forward[i + 1] = max(forward[i + 1], forward[i] + values[i + 1])
    forward[i + 2] = max(forward[i + 2], forward[i] + values[i + 2])
if n > 1:
    forward[n - 1] = max(forward[n - 1], forward[n - 2] + values[n - 1])

max_score = MIN_VAL
if dry_run:
    for i in range(k, n):
        for_score = forward[i] - forward[k]
        back_score = backward[i] - values[i]
        score = for_score + back_score
        print("Going till : %2d | forward_score : %5d, backward_score : %5d, total_score : %5d" % (i, for_score, back_score, score))
        max_score = max(max_score, score)
else:
    for i in range(k, n):
        for_score = forward[i] - forward[k]
        back_score = backward[i] - values[i]
        score = for_score + back_score
        max_score = max(max_score, score)

if dry_run:
    print('k              :', k)
    print('values         :', values)
    print('backward       :', backward)
    print('score max      :', max_score)

print(max_score)
