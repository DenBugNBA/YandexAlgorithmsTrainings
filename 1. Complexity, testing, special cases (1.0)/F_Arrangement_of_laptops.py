def calculte_table_size(length1, width1, length2, width2):
    min1 = min(length1, width1)
    max1 = max(length1, width1)

    min2 = min(length2, width2)
    max2 = max(length2, width2)

    square_from_mins = (min1 + min2) * max((max1, max2))

    square_from_max_and_min = 0

    if max1 > max2:
        square_from_max_and_min = (max1 + min2) * max(min1, max2)
    else:
        square_from_max_and_min = (max2 + min1) * max(min2, max1)

    if square_from_mins < square_from_max_and_min:
        return min1 + min2, max(max1, max2)
    else:
        if max1 > max2:
            return max1 + min2, max(min1, max2)
        else:
            return max2 + min1, max(min2, max1)


if __name__ == "__main__":
    length1, width1, length2, width2 = map(int, input().split())

    # Любой из:
    # 20 2
    # 2 20
    # 4 10
    # 10 4
    # length1, width1, length2, width2 = 10, 2, 2, 10

    # Любой из:
    # 9 5
    # 5 9
    # length1, width1, length2, width2 = 5, 7, 3, 2

    print(*calculte_table_size(length1, width1, length2, width2))
