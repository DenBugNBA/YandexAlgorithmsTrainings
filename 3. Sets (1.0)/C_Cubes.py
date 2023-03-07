def cubes(n_nums, m_nums):
    s1 = set(n_nums)
    s2 = set(m_nums)

    both = sorted(s1 & s2)
    both_len = len(both)

    first_rest = sorted(s1 - s2)
    first_rest_len = len(first_rest)

    second_rest = sorted(s2 - s1)
    second_rest_len = len(second_rest)

    return (both_len, both, first_rest_len, first_rest, second_rest_len, second_rest)


if __name__ == "__main__":
    n, m = map(int, input().split())
    n_nums = []
    for _ in range(n):
        n_nums.append(int(input()))
    m_nums = []
    for _ in range(m):
        m_nums.append(int(input()))

    # 2
    # 0 1
    # 2
    # 9 10
    # 1
    # 3
    # n_nums = [0, 1, 10, 9]
    # m_nums = [1, 3, 0]

    # 1
    # 2
    # 1
    # 1
    # 1
    # 3
    # n_nums = [1, 2]
    # m_nums = [2, 3]

    res = cubes(n_nums, m_nums)
    for i in range(0, len(res), 2):
        print(res[i])
        print(*res[i + 1])

"""
0

0

0

"""
"""
0 0
"""
