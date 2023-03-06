def check_is_covering(l, params):
    n, k, coordinates = params

    current_segments = 0

    left = 0
    while left < n:
        current_x = coordinates[left]
        current_segments += 1
        x_plus_shift = current_x + l
        while left < n and x_plus_shift >= coordinates[left]:
            left += 1

    return k >= current_segments


def binary_search(left, right, check, params):
    while left < right:
        m = (left + right) // 2
        if check(m, params):
            right = m
        else:
            left = m + 1
    return left


def count_min_segments(n, k, coordinates):
    l = binary_search(0, 10**10, check_is_covering, (n, k, coordinates))
    return l


if __name__ == "__main__":
    n, k = map(int, input().split())
    coordinates = sorted(list(map(int, input().split())))

    # 2
    # n, k = 6, 2
    # coordinates = [1, 2, 3, 7, 8, 9]

    # 1
    # n, k = 1, 1
    # coordinates = [-11]

    print(count_min_segments(n, k, coordinates))
