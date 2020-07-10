MIN_VAL = -10000000001
n, k = map(int, input().split())
array = [int(i) for i in input().split()]

arr1 = [MIN_VAL] * n
arr2 = [MIN_VAL] * n
k -= 1

arr1[0] = array[0]
for i in range(n - 2):
    arr1[i + 1] = max(arr1[i + 1], arr1[i] + array[i + 1])
    arr1[i + 2] = max(arr1[i + 2], arr1[i] + array[i + 2])
if n > 1:
    arr1[n - 1] = max(arr1[n - 1], arr1[n - 2] + array[n - 1])

arr2[k] = array[k]
for i in range(k, n - 2):
    arr2[i + 1] = max(arr2[i + 1], arr2[i] + array[i + 1])
    arr2[i + 2] = max(arr2[i + 2], arr2[i] + array[i + 2])
if n > 1:
    arr2[n - 1] = max(arr2[n - 1], arr2[n - 2] + array[n - 1])

max_score = MIN_VAL
for i in range(k, n):
    max_score = max(max_score, arr1[i] + arr2[i] - array[i] - arr2[k])

print(max_score)