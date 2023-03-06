def check_greater_equal(days, params):
    a, k, b, m, x = params
    first_woodcutter = (a * days) - ((days // k) * a)
    second_woodcutter = (b * days) - ((days // m) * b)

    return first_woodcutter + second_woodcutter >= x


def binary_search(left, right, check, params):
    while left < right:
        m = (left + right) // 2
        if check(m, params):
            right = m
        else:
            left = m + 1
    return left


def count_days(a, k, b, m, x):
    days = binary_search(1, 10**19, check_greater_equal, (a, k, b, m, x))
    return days


if __name__ == "__main__":
    a, k, b, m, x = map(int, input().split())

    # 8
    # a, k, b, m, x = 1, 2, 1, 3, 10

    # 9
    # a, k, b, m, x = 1, 2, 1, 3, 11

    # 4
    # a, k, b, m, x = 19, 3, 14, 6, 113

    # 7
    # a, k, b, m, x = 2, 4, 3, 3, 25

    print(count_days(a, k, b, m, x))
