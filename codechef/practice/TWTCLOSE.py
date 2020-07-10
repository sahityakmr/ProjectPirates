n, k = map(int, input().split())
# Defining List
list = []
count = 0
for i in range(k):
    str = input()
    if str == 'CLOSEALL':
        # Clearing List
        list.clear()
        count = 0
    else:
        text, num = str.split()
        number = int(num)
        if number in list:
            # finding index in list
            index = list.index(number)
            del list[index]
            count -= 1
        else:
            # inserting in list
            list.append(number)
            count += 1
    print(count)
