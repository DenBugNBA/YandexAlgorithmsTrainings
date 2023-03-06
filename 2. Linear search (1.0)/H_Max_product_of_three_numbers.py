def find_two_minimums(arr):
    min1 = min(arr[0], arr[1])
    min2 = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return min1, min2


def sort_two_nums(a, b):
    if a > b:
        return a, b
    return b, a


def find_three_maximums(arr):
    max1, max2, max3 = arr[0], arr[1], arr[2]
    max1, max2 = sort_two_nums(max1, max2)
    max1, max3 = sort_two_nums(max1, max3)
    max2, max3 = sort_two_nums(max2, max3)

    for i in range(3, len(arr)):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3:
            max3 = arr[i]

    return max1, max2, max3


def max_product_of_three(arr):
    if len(arr) <= 3:
        return arr

    max1, max2, max3 = find_three_maximums(arr)
    min1, min2 = find_two_minimums(arr)

    if max1 * max2 * max3 > min1 * min2 * max1:
        return max1, max2, max3
    else:
        return min1, min2, max1


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    # 10 9 9
    # arr = [3, 5, 1, 7, 9, 0, 9, -3, 10]

    # -5 -30000 -12
    # arr = [-5, -30000, -12]

    # 1 2 3
    # arr = [1, 2, 3]

    # 5 5 4
    # arr = [4, 3, 5, 2, 5]

    # -5 -4 5
    # arr = [-4, 3, -5, 2, 5]

    # 1 -1 1
    # arr = [1, -1, 1]

    # -7 -7 10
    # arr = [4, -7, -4, 0, 10, 9, -7, -1]

    # 29710 24431 15992
    # arr = [12288, -10075, 29710, 15686, -18900, -17715, 15992, 24431]

    result = max_product_of_three(arr)
    print(*result)
