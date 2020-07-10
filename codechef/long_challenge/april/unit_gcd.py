for t in range(int(input())):
    n = int(input())

    k = int(n/2)
    if n < 2:
        k = 1
    data = str(k) + "\n"

    for i in range(n, 3, -2):
        data += "2 " + str(i) + " " + str(i - 1) + "\n"

    if n % 2 == 0:
        data += "2 1 2"
    elif n == 1:
        data += "1 1"
    else:
        data += "3 1 2 3"
    print(data)
