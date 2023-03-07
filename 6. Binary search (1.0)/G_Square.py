def check_is_enough_tiles(width_of_path, params):
    n, m, t = params

    square = n * m

    n_new = n - (width_of_path * 2)
    m_new = m - (width_of_path * 2)

    if n_new > 0 and m_new > 0:
        empty_space = n_new * m_new
        return empty_space < square and t >= (square - empty_space)
    return False


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right + 1) // 2

        if check(mid, params):
            left = mid
        else:
            right = mid - 1

    return left


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    t = int(input())

    # 2
    # n = 6
    # m = 7
    # t = 38

    print(binary_search(0, 10**30, check_is_enough_tiles, (n, m, t)))
