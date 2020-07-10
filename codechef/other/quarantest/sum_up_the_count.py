n = int(input())
diction = dict()
for i in input().split():
    k = int(i)
    if diction.get(k) is None:
        diction[k] = 1
    else:
        diction[k] += 1
# print(diction)

for key in diction:
    print(key + diction[key], end=' ')