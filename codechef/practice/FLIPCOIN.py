n, q = map(int, input().split())
arr = []
i = 0
for i in range(n):
    arr.append('T')


def rev():
    if arr[i] == 'H':
        arr[i] = 'T'
    else:
        arr[i] = 'H'


while q > 0:
    command, first, last = map(int, input().split())
    if command == 0:
        for i in range(first, last+1):
            rev()
    elif command == 1:
        count = 0
        for i in range(first, last+1):
            if arr[i] == 'H':
                count += 1
        print(count)
    q -= 1
