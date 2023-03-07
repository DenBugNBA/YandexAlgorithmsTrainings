def check_is_bigger_equal(seconds, params):
    # нужно n копий, ксероксы копируют x и y секунд
    n, x, y = params

    copies_count = 1
    seconds -= min(x, y)

    copies_count += seconds // x + seconds // y

    return copies_count >= n


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right) // 2

        if check(mid, params):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    n, x, y = map(int, input().split())

    # 3
    # n, x, y = 4, 1, 1

    # 4
    # n, x, y = 5, 1, 2

    print(binary_search(0, 10**30, check_is_bigger_equal, (n, x, y)))
