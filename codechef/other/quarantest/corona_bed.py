config = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
src_r, src_c = 3, 0
des_r, des_c = 0, 3
total_r, total_c = 4, 4
visited = [[0 for i in range(4)] for j in range(4)]
possible_row_moves = [-1, 0, 1, 0]
possible_col_moves = [0, -1, 0, 1]


def try_exit(curr_r, curr_c, path):
    if curr_r == des_r and curr_c == des_c:
        print("len  : %2d | path : %s" % (len(path.split('->')), path))
        return
    for i in range(4):
        next_r, next_c = curr_r + possible_row_moves[i], curr_c + possible_col_moves[i]
        if 0 <= next_r < total_r and 0 <= next_c < total_c and visited[next_r][next_c] != 1:
            if not (next_r == src_r and next_c == src_c):
                visited[next_r][next_c] = 1
            try_exit(next_r, next_c, path + "->" + str(config[next_r][next_c]))
            visited[next_r][next_c] = 0


try_exit(src_r, src_c, str(13))
