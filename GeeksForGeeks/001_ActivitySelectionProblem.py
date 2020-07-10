'''

You are given n activities with their start and finish times.
 Select the maximum number of activities that can be performed
  by a single person, assuming that a person can only work on
   a single activity at a time.

'''


n = int(input("Enter number of activities"))
startTimes = [int(i) for i in input().split()]
finishTimes = [int(i) for i in input().split()]
for i in range(0,len(startTimes)):
    for j in range(0,len(startTimes)-i-1):
        if  finishTimes[j]>finishTimes[j+1]:
            temp1 = finishTimes[j + 1]
            temp2 = startTimes[j+1]
            finishTimes[j+1] = finishTimes[j]
            startTimes[j+1] = startTimes[j]
            finishTimes[j] = temp1
            startTimes[j] = temp2
j=0
print('(',startTimes[0],',',finishTimes[0],'),')
for i in range(1, len(startTimes)):
    if startTimes[i]>=finishTimes[j]:
        print('(',startTimes[i],',',finishTimes[i],'),')
        j += 1


