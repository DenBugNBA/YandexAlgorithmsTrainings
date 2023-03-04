def count_max_subarray(a, n):
    max_sum = a[0]
    current_sum = a[0]

    for i in range(1, n):
        num = a[i]
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    # 10
    # n = 4
    # a = [1, 2, 3, 4]

    # 9
    # n = 4
    # a = [5, 4, -10, 4]

    print(count_max_subarray(a, n))
