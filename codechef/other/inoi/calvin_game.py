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

forward = [-1000000001] * n
backward = [-1000000001] * n
score_one = 0
score_two = score_three = -1000000001
k -= 1


def fill_forward_on():
    forward[n - 1] = values[n - 1]
    for i in range(n - 1, 1, -1):
        forward[i - 1] = max(forward[i - 1], forward[i] + values[i - 1], values[i - 1])
        forward[i - 2] = max(forward[i - 2], forward[i] + values[i - 2], values[i - 2])
    if n > 1:
        forward[0] = max(forward[0], forward[1] + values[0], values[0])


def fill_backward_on():
    backward[0] = values[0]
    for i in range(n - 2):
        backward[i + 1] = max(backward[i + 1], backward[i] + values[i + 1])
        backward[i + 2] = max(backward[i + 2], backward[i] + values[i + 2])
    if n > 1:
        backward[n - 1] = max(backward[n - 1], backward[n - 2] + values[n - 1])


fill_forward_on()
fill_backward_on()

# case 1
for_score = forward[k] - values[k]

back_score = 0

first_neg = k + 1
while first_neg < n and forward[first_neg] >= 0:
    first_neg += 1

back_score = backward[first_neg - 1] - values[first_neg - 1]

# avoid moving forward even on positive score
score_two = backward[k] - values[k]
if k < n - 1:
    score_three = backward[k + 1]

# avoid going backward even on negative score

score_one = for_score + back_score

max_score = -1000000001
for i in range(k, n):
    score = backward[i] - backward[k]
    if i > 0:
        score += backward[i - 1]
    max_score = max(max_score,  score)

if dry_run:
    print('k              :', k)
    print('values         :', values)
    print('forward        :', forward)
    print('backward       :', backward)
    print('forward score  :', for_score)
    print('first -ve      :', first_neg)
    print('backward score :', back_score)
    print('score one      :', score_one)
    print('score two      :', score_two)
    print('score three    :', score_three)
    print('score max      :', max_score)

# print(max(score_one, score_two, score_three))
print(max_score)

'''
cases : 
    1. move forward and move backward
    2. move backward

'''
