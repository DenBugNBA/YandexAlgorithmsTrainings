def count_number_of_groups(x, y, n, m):
    groups_spread = 0
    result_auditoriums = [0] * n

    x_sorted = sorted(enumerate(x), key=lambda t: t[1])
    y_sorted = sorted(enumerate(y), key=lambda t: t[1])

    audience_pointer = 0

    for index, students_count in x_sorted:
        while audience_pointer < m and students_count >= y_sorted[audience_pointer][1]:
            audience_pointer += 1
        if audience_pointer < m and y_sorted[audience_pointer][1] > students_count:
            result_auditoriums[index] = y_sorted[audience_pointer][0] + 1
            groups_spread += 1
            audience_pointer += 1

    print(groups_spread)
    print(*result_auditoriums)


if __name__ == "__main__":
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    # 1
    # 1
    # n, m = 1, 1
    # x = [1]
    # y = [2]

    # 0
    # 0
    # n, m = 1, 1
    # x = [1]
    # y = [1]

    # 2
    # 0 1 3
    # n, m = 3, 3
    # x = [10, 3, 4]
    # y = [4, 4, 5]

    # 3
    # 0 2 4 1
    # n, m = 4, 4
    # x = [10, 3, 4, 1]
    # y = [2, 4, 4, 5]

    # 1
    # 3
    # n, m = 1, 3
    # x = [2]
    # y = [1, 2, 3]

    # 4
    # 1 2 3 4
    # n, m = 4, 4
    # x = [1, 1, 1, 1]
    # y = [2, 2, 2, 2]

    count_number_of_groups(x, y, n, m)
