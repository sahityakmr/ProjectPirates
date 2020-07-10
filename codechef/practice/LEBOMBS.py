t = int(input())
while t > 0:
    n = int(input())
    str1 = input()
    string1 = []
    string2 = []
    for l in str1:
        string1.append(l)
        string2.append(l)
    if len(string1) > 1:
        for i in range(len(string1)):
            if string1[i] == '1':
                if i == 0:
                    string2[i + 1] = '1'
                elif i == len(string1)-1:
                    string2[i - 1] = '1'
                else:
                    string2[i - 1] = string2[i + 1] = '1'
    count = 0
    for l in string2:
        if l == '0':
            count = count + 1
    print(count)
    t = t - 1