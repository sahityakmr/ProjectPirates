t = int(input())
while t>0:
    n = int(input())
    zeros = 0
    while n>=5:
        n = int(n/5)
        zeros += n
    print(int(zeros))
    t -= 1