n = int(input())
numbers = [int(n) for n in input().split()]
cycle = []
count = 0
output = ""
for k in range(0, n):
    i = k
    if i in cycle:
        continue
    while i not in cycle:
        output = output + str(i+1)+" "
        cycle.append(i)
        i = numbers[i] - 1
        output = output + str(i+1) + "\n"
        count = count + 1
print(count)
print(output)
