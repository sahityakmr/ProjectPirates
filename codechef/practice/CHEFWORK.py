n = int(input())
c = [int(i) for i in input().split()]
#t = [int(i) for i in input().split()]
t = []
minOne = 100001
minTwo = 100001
minThree = 100001
cur = 0
for i in input().split():
    k = int(i)
    l = c[cur]
    if k == 1 and l<minOne:
        minOne = l
    if k == 2 and l<minTwo:
        minTwo = l
    if k == 3 and l<minThree:
        minThree = l
    cur += 1
print(min(minOne+minTwo,minThree))