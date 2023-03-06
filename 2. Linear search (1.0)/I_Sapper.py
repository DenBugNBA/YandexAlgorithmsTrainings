def create_sapper_field(n, m, k, bombs):
    field = []

    for _ in range(n):
        line = [0] * m
        field.append(line)

    if k == 0:
        return field

    for bomb in bombs:
        field[bomb[0] - 1][bomb[1] - 1] = "*"

    for i in range(len(field)):
        line = field[i]

        for j in range(len(line)):
            if field[i][j] != "*":
                count = 0
                start = [i - 1, j - 1]
                end = [i + 1, j + 1]

                if i == 0:
                    start[0] = i
                if i == len(field) - 1:
                    end[0] = i
                if j == 0:
                    start[1] = j
                if j == len(line) - 1:
                    end[1] = j

                for k in range(start[0], end[0] + 1):
                    for l in range(start[1], end[1] + 1):
                        if field[k][l] == "*":
                            count += 1

                field[i][j] = count

    return field


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    bombs = []
    for _ in range(k):
        x, y = map(int, input().split())
        bombs.append((x, y))

    """
    * 2
    2 *
    1 1
    """
    # n, m, k = 3, 2, 2
    # bombs = [(1, 1), (2, 2)]

    """
    0 0
    0 0
    """
    # n, m, k = 2, 2, 0
    # bombs = []

    """
    1 2 * 1
    * 2 1 1
    2 2 2 1
    1 * 2 *
    """
    # n, m, k = 4, 4, 4
    # bombs = [(1, 3), (2, 1), (4, 2), (4, 4)]

    field = create_sapper_field(n, m, k, bombs)

    for line in field:
        print(*line)
