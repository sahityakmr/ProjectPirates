t = int(input())
while t > 0:
    n = int(input())
    A = [int(i) for i in input().split()]
    index = A.index(max(A))
    t -= 1