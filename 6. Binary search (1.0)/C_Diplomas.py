def check_size(size, params):
    w, h, n = params
    return (size // w) * (size // h) >= n


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right) // 2
        if check(mid, params):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    w, h, n = map(int, input().split())

    # 9
    # w, h, n = 2, 3, 10

    billion = 1000000000
    print(binary_search(0, billion * billion, check_size, (w, h, n)))
