import sys

dry_run = False
if dry_run:
    file = open('res/covid_sampling.txt')
    sys.stdin = file

global mat


def size(from_row, from_col, to_row, to_col):
    return (to_row - from_row + 1) * (to_col - from_col + 1)


def fill(from_row, from_col, to_row, to_col):
    for row in range(from_row, to_row + 1):
        for col in range(from_col, to_col + 1):
            mat[row][col] = 1


def solve(from_row, from_col, to_row, to_col, mat_count, vertical, only_v, only_h):
    if vertical:
        # splitting vertically
        if from_row < to_row:
            # multiple rows
            mid_row = int((to_row + from_row) / 2)
            print(1, from_row, from_col, mid_row, to_col)
            top_half = int(input())

            if top_half == size(from_row, from_col, mid_row, to_col):
                fill(from_row, from_col, mid_row, to_col)
            elif top_half > 0:
                direction = not vertical
                if only_v:
                    direction = True
                if only_h:
                    direction = False
                solve(from_row, from_col, mid_row, to_col, top_half, direction, only_v, only_h)

            if top_half < mat_count:
                # bottom half also has elements
                bottom_half = mat_count - top_half
                if bottom_half == size(mid_row + 1, from_col, to_row, to_col):
                    fill(mid_row + 1, from_col, to_row, to_col)
                elif bottom_half > 0:
                    direction = not vertical
                    if only_v:
                        direction = True
                    if only_h:
                        direction = False
                    solve(mid_row + 1, from_col, to_row, to_col, bottom_half, direction, only_v, only_h)
        else:
            # single row
            solve(from_row, from_col, to_row, to_col, mat_count, False, only_v, True)

    else:
        # splitting horizontally
        if from_col < to_col:
            # multiple columns
            mid_col = int((to_col + from_col) / 2)

            print(1, from_row, from_col, to_row, mid_col)
            left_half = int(input())
            if left_half == size(from_row, from_col, to_row, mid_col):
                fill(from_row, from_col, to_row, mid_col)
            elif left_half > 0:
                direction = not vertical
                if only_v:
                    direction = True
                if only_h:
                    direction = False
                solve(from_row, from_col, to_row, mid_col, left_half, direction, only_v, only_h)

            if left_half < mat_count:
                # right half also has elements
                right_half = mat_count - left_half
                if right_half == size(from_row, mid_col + 1, to_row, to_col):
                    fill(from_row, mid_col + 1, to_row, to_col)
                elif right_half > 0:
                    direction = not vertical
                    if only_v:
                        direction = True
                    if only_h:
                        direction = False
                    solve(from_row, mid_col + 1, to_row, to_col, right_half, direction, only_v, only_h)
        else:
            # single column
            solve(from_row, from_col, to_row, to_col, mat_count, True, True, only_h)


for t in range(int(input())):
    n, p = map(int, input().split())
    mat = [[0 for i in range(n + 1)] for j in range(n + 1)]
    print(1, 1, 1, n, n)
    total = int(input())
    solve(1, 1, n, n, total, True, False, False)
    print(2)
    mat = mat[1:]
    for _row in mat:
        print(" ".join(str(r) for r in _row[1:]))
    x = int(input())
    if x == -1:
        break
    pass
