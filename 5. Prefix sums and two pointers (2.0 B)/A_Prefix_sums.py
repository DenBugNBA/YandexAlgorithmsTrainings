def get_prefix_sum(a, n):
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    return prefix_sum


def range_sum_query(prefix_sum, left, right):
    return prefix_sum[right] - prefix_sum[left - 1]


if __name__ == "__main__":
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    prefix_sum = get_prefix_sum(a, n)

    for _ in range(q):
        left, right = map(int, input().split())
        print(range_sum_query(prefix_sum, left, right))

# 1
# 3
# 6
# 10
# 2
# 5
# 9
# 3
# 7
# 4
"""
4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""
