T = int(input())

while T>0:
    count = 0
    n,a,b,c = map(int,input().split())
    li = []

    def fun(factors, len, x, y, z):
        if len == 0:
            if [x, y, z] not in li:
                li.append([x, y, z])
            return
        if x not in range(1, a) \
                or y not in range(1, b) \
                or z not in range(1, c):
            return

        fun(factors, len - 1, x * factors[len - 1], y, z)
        fun(factors, len - 1, x, y * factors[len - 1], z)
        fun(factors, len - 1, x, y, z * factors[len - 1])
        return

    factors = []
    for i in range(2,n+1):
        while n%i == 0:
            factors.append(i)
            n /= i
        if n == 1:
            break
    print(factors)
    fun(factors,len(factors),1,1,1)
    print(li)
    T -= 1