def check_is_greater_equal(index, params):
    l, nums = params
    return nums[index] >= l


def check_is_greater(index, params):
    r, nums = params
    return nums[index] > r


def binary_search(left, right, check, params):
    while left < right:
        m = (left + right) // 2

        if check(m, params):
            right = m
        else:
            left = m + 1

    return left


def count_nums_between(l, r, nums, n):
    l_index = binary_search(0, n - 1, check_is_greater_equal, (l, nums))

    if nums[l_index] < l:
        return 0

    r_index = binary_search(0, n - 1, check_is_greater, (r, nums))

    if nums[r_index] > r:
        r_index -= 1

    return r_index - l_index + 1


if __name__ == "__main__":
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        print(count_nums_between(l, r, nums, n))


# 5 2 2 0
"""
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2
"""
