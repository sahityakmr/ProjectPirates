t = int(input())
while t>0:
    print(input().replace('<','#').replace('>','<').replace('#','>').count('><'))
    t -= 1