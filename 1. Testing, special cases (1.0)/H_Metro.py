def count_time_waiting(interval_1, interval_2, count_1, count_2):
    if interval_1 <= 0 or interval_2 <= 0 or count_1 <= 0 or count_2 <= 0:
        return -1
    if interval_1 < interval_2 and count_1 < count_2:
        return -1
    if interval_2 < interval_1 and count_2 < count_1:
        return -1

    min_1 = count_1 + (count_1 - 1) * interval_1
    min_2 = count_2 + (count_2 - 1) * interval_2

    max_1 = count_1 + (count_1 + 1) * interval_1
    max_2 = count_2 + (count_2 + 1) * interval_2

    return max(min_1, min_2), min(max_1, max_2)


if __name__ == "__main__":
    interval_1 = int(input())
    interval_2 = int(input())
    count_1 = int(input())
    count_2 = int(input())

    # 5 7
    # interval_1 = 1
    # interval_2 = 3
    # count_1 = 3
    # count_2 = 2

    # -1
    # interval_1 = 1
    # interval_2 = 5
    # count_1 = 1
    # count_2 = 2

    # -1
    # interval_1 = 0
    # interval_2 = 0
    # count_1 = 0
    # count_2 = 0

    result = count_time_waiting(interval_1, interval_2, count_1, count_2)
    if isinstance(result, tuple):
        print(result[0], result[1])
    else:
        print(result)
