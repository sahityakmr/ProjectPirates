import math
n, r = map(int, input().split())
homes = [int(i) for i in input().split()]
arr = [abs(r - i) for i in homes]
# print(arr)
k = arr[0]
for i in range(1, len(arr)):
    k = math.gcd(k, arr[i])
print(k)