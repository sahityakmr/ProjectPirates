t = int(input())
while t > 0:
    n = int(input())
    numbers = [int(n) for n in input().split()]
    count = 0
    for i in range(n):
        for j in range(n):
            if (numbers[i] <= n) and (numbers[i] >= 1) and (numbers[j] <= n) and (numbers[j] >= 1) and (numbers[i] < numbers[j]):
                count += 1
    print(count)
    t -= 1
