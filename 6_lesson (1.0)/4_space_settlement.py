def check_size(d, params):
    n, a, b, w, h = params

    horizontally_max_n = (w // (a + 2 * d)) * (h // (b + 2 * d))
    vertically_max_n = (w // (b + 2 * d)) * (h // (a + 2 * d))

    return horizontally_max_n >= n or vertically_max_n >= n


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right + 1) // 2

        if check(mid, params):
            left = mid
        else:
            right = mid - 1

    return left


n, a, b, w, h = map(int, input().split())

# n, a, b, w, h = 1, 1, 1, 1, 1  # 0
# n, a, b, w, h = 1, 1, 1, 3, 3  # 1
# n, a, b, w, h = 11, 3, 2, 21, 25  # 2

billion = 1000000000
print(binary_search(0, billion**5, check_size, (n, a, b, w, h)))
