N = int(input())
while N>0:
    sol = [int(i) for i in input().split()]
    count = 0
    for s in sol:
        if s==1:
            count += 1
    if count == 0:
        print("Beginner")
    if count == 2:
        print("Middle Developer")
    if count == 1:
        print("Junior Developer")
    if count == 3:
        print("Senior Developer")
    if count == 4:
        print("Hacker")
    if count == 5:
        print("Jeff Dean")
    N -= 1