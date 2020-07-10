t = int(input())
while t > 0:
    n, k = map(int, input().split())
    numbers = [int(n) for n in input().split()]
    sum2 = sum1 = 0
    numbers = sorted(numbers)
    for i in range(k):
        sum2 = sum2 + numbers[i]
    for i in range(k, len(numbers)):
        sum1 = sum1 + numbers[i]
    print(abs(sum1-sum2))
    t = t-1
