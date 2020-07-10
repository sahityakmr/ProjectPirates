import sys

dry_run = True
if dry_run:
    input_file = open('res/chef_and_price_control.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    n, k = map(int, input().split())
    prices = [int(i) for i in input().split()]
    loss = 0
    for price in prices:
        if price > k:
            loss += price - k
    print(loss)
    pass
