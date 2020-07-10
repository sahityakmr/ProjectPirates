for t in range(int(input())):
    n, m, k = map(int, input().split())
    answers = []
    for i in range(n):
        answers.append([int(i) for i in input().split()])
    weightage = [0 for i in range(k + 1)]
    probability = [0 for i in range(m + 1)]
    for row in answers:
        for val in row:
            probability[val] += 1
    print(answers)
