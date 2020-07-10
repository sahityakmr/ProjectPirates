def prime(x):
    lst = []
    while x > 1:
        for i in range(2, x + 1):
            if x % i == 0:
                lst.append(i)
                x /= i
                break
    return lst


def all(x):
    lst = []
    for i in range(1, x + 1):
        if x % i == 0:
            lst.append(i)
    return lst


print(all(105))
print(prime(105))
