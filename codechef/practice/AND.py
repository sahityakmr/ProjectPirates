n = int(input())
array = [int(i) for i in input().split()]
sum = 0
for i in range(n):
    for j in range(i+1,n):
        sum += array[i]&array[j]
print(sum)