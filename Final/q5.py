def rotate(m):
    temp = [[m[j][i] for j in range(len(m) - 1, -1, -1)] for i in range(0, len(m), 1)]
    return temp


def print_mat(m):
    for row in m:
        print(' '.join(row))


if __name__ == '__main__':
    sq_mat = []
    sq_mat.append(input().split())
    for i in range(1, len(sq_mat[0])):
        sq_mat.append(input().split())
    print_mat(rotate(sq_mat))
