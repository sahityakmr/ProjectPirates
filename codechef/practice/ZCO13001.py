n = int(input())
strengths = [int(i) for i in input().split()]
strengths = sorted(strengths)
cumm_strengths = [0]*n
cumm_strengths[n-1] = strengths[n-1]
for i in range(n-2,0,-1):
    cumm_strengths[i] = cumm_strengths[i+1]+strengths[i]
for i in range(1,n):
    cumm_strengths[i] -= (n-i)*strengths[i-1]
print(sum(cumm_strengths))
