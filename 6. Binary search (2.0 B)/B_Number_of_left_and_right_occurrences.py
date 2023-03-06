def check_is_greater_equal(index, params):
    num, arr = params
    return arr[index] >= num


def check_is_greater(index, params):
    num, arr = params
    return arr[index] > num


def binary_search(left, right, check, params):
    while left < right:
        m = (left + right) // 2
        if check(m, params):
            right = m
        else:
            left = m + 1
    return left


def get_left_and_right_position(num, arr, n):
    left_position = binary_search(0, n - 1, check_is_greater_equal, (num, arr))

    if arr[left_position] != num:
        return 0, 0

    right_position = binary_search(0, n - 1, check_is_greater, (num, arr))

    if arr[right_position] != num:
        right_position -= 1

    return (left_position + 1, right_position + 1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    find_arr = list(map(int, input().split()))

    seen_nums = {}
    for num in find_arr:
        if num not in seen_nums:
            seen_nums[num] = get_left_and_right_position(num, arr, n)

        print(*seen_nums[num])

# 0 0
# 4 4
# 2 3
# 1 1
"""
4
1 2 2 3
4
4 3 2 1
"""

# 7 8
# 3 3
# 3 3
# 1 1
# 3 3
# 7 8
# 10 10
# 7 8
# 7 8
# 0 0
"""
10
1 2 3 4 5 6 7 7 8 9
10
7 3 3 1 3 7 9 7 7 10
"""

# 0 0
# 9 9
# 6 6
# 0 0
# 0 0
# 9 9
# 2 5
# 0 0
# 9 9
# 0 0
"""
10
1 3 3 3 3 6 8 8 9 10
10
2 9 6 4 2 9 3 7 9 7
"""
