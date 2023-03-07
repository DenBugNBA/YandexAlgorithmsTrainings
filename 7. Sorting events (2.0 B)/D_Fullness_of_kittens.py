def make_prefix_sum_kittens(a):
    prefix_sum_kittens = [[-1, 0]]

    for i in range(n):
        if i != 0 and a[i] == a[i - 1]:
            prefix_sum_kittens[-1][1] += 1
        else:
            prefix_sum_kittens.append([a[i], prefix_sum_kittens[-1][1] + 1])

    return prefix_sum_kittens


def check_greater_equal(index, params):
    l, prefix_sum_kittens = params
    return prefix_sum_kittens[index][0] >= l


def check_greater(index, params):
    r, prefix_sum_kittens = params
    return prefix_sum_kittens[index][0] > r


def binary_search(left, right, check, params):
    while left < right:
        m = (left + right) // 2
        if check(m, params):
            right = m
        else:
            left = m + 1
    return left


def count_fullness_of_kittens(l, r, prefix_sum_kittens):
    left_index = binary_search(
        0,
        len(prefix_sum_kittens) - 1,
        check_greater_equal,
        (l, prefix_sum_kittens),
    )

    right_index = binary_search(
        0,
        len(prefix_sum_kittens) - 1,
        check_greater,
        (r, prefix_sum_kittens),
    )

    if left_index == right_index:
        if (
            prefix_sum_kittens[right_index][0] > r
            or prefix_sum_kittens[right_index][0] < l
        ):
            return 0
        else:
            return (
                prefix_sum_kittens[right_index][1]
                - prefix_sum_kittens[right_index - 1][1]
            )
    else:
        if prefix_sum_kittens[left_index][0] >= l:
            left_index -= 1

        if prefix_sum_kittens[right_index][0] > r:
            right_index -= 1

        if left_index == right_index:
            return prefix_sum_kittens[right_index][1]
        else:
            return (
                prefix_sum_kittens[right_index][1] - prefix_sum_kittens[left_index][1]
            )


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    prefix_sum_kittens = make_prefix_sum_kittens(a)

    for _ in range(m):
        l, r = map(int, input().split())

        print(count_fullness_of_kittens(l, r, prefix_sum_kittens))


# 5
# 5
"""
6 2
0 2 3 4 4 6
0 4
2 7
"""

# 5
# 4
"""
5 2
1 2 3 1 1
1 7
1 2
"""

# 5
"""
5 1
1 1 1 1 1
1 1
"""

# 0
"""
3 1  
3 5 4
0 2
"""

# 1
"""
2 1
2 7
0 2
"""

# 0
"""
2 1
4 4
6 7
"""

# 2
"""
5 1
0 2 2 3 3
3 6
"""

# 5
"""
5 1
1 3 5 6 7
0 7
"""
