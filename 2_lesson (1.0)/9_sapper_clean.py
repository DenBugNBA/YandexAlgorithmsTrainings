# n, m, k = map(int, input().split())
# bombs = []
# for _ in range(k):
#     x, y = map(int, input().split())
#     bombs.append((x, y))

# n, m, k = 4, 4, 4
# bombs = [(1, 3), (2, 1), (4, 2), (4, 4)]

# n, m, k = 2, 2, 0
# bombs = []

n, m, k = 3, 2, 2
bombs = [(1, 1), (2, 2)]


def create_sapper_field(n, m, bombs):
    field = []

    for _ in range(n + 2):
        field.append([0] * (m + 2))

    di = (1, 1, 1, 0, 0, -1, -1, -1)
    dj = (-1, 0, 1, -1, 1, -1, 0, 1)

    for i, j in bombs:
        for k in range(8):
            field[i + di[k]][j + dj[k]] += 1

    for i, j in bombs:
        field[i][j] = "*"

    return field


field = create_sapper_field(n, m, bombs)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(field[i][j], end=" ")
    print()
