import sys

dry_run = True
if dry_run:
    input_file = open('res/chef_and_string.txt')
    sys.stdin = input_file

global var
for t in range(int(input())):
    s = input()
    last = s[0]
    pairs = 0
    for i in range(1, len(s)):
        c = s[i]
        if c == 'x' and last == 'y':
            pairs += 1
            last = None
        elif c == 'y' and last == 'x':
            pairs += 1
            last = None
        else:
            last = c
    print(pairs)
    pass
