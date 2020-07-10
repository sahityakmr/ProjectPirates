t = int(input())
while t>0:
    x,p = input().split()
    n = int(x)
    A = [int(i) for i in input().split()]
    if n==1 and A[0]%2==0 and p == "Dee":
        print("Dee")
    else:
        print("Dum")
    t -= 1