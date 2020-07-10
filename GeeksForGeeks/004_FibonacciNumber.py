#recursive approach
def fibR(n):
    if n <= 1:
        return n
    return fibR(n - 1) + fibR(n - 2)

#storage approach
def fibS(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    print(a[n])

#without storage
def fibWS(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return b
n = 9
#printing through recursive call
print(fibR(n))

#printing through storage
fibS(n)

#printing without storage
print(fibWS(n))