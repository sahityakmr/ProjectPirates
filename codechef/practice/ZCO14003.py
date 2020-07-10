budget = []
n = int(input())
t = n
while t > 0:
    budget.append(int(input()))
    t -= 1
budget = sorted(budget)
max=0
for i in range(n):
    k = budget[i]*(n-i)
    if k>max:
        max = k
print(max)