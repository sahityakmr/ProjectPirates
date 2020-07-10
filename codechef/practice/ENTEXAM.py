t = int(input())
while t>0:
    n,k,e,m = map(int,input().split())
    marks = []
    for i in range(n-1):
        s = sum([int(i) for i in input().split()])
        marks.append(s)
    myMarks = sum([int(i) for i in input().split()])
    #print(marks)
    marks = sorted(marks,reverse=True)
    #print(marks)
    reqMarks = marks[k-1]+1-myMarks
    if reqMarks>m:
        print("Impossible")
    elif reqMarks<0:
        print(0)
    else:
        print(reqMarks)
    t -= 1