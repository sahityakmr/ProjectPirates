n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array = sorted(array)
for i in range(n):
    print(array[i])