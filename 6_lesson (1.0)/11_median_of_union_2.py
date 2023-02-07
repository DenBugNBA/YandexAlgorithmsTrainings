def check_is_greater_equal(index, params):
    arr, x = params
    return arr[index] >= x


def left_binary_search(left, right, check, params):
    while left < right:
        mid = (left + right) // 2

        if check(mid, params):
            right = mid
        else:
            left = mid + 1

    return left


def count_less(arr, x):
    res = left_binary_search(0, len(arr) - 1, check_is_greater_equal, (arr, x))
    if arr[res] < x:
        return len(arr)
    return res


def count_greater(arr, x):
    return len(arr) - count_less(arr, x + 1)


def count_left_median(arr1, arr2):
    left = min(arr1[0], arr2[0])
    right = max(arr1[-1], arr2[-1])

    while left < right:
        mid = (left + right) // 2
        less = count_less(arr1, mid) + count_less(arr2, mid)
        greater = count_greater(arr1, mid) + count_greater(arr2, mid)

        if less <= len(arr1) - 1 and greater <= len(arr1):
            return mid
        if greater > len(arr1):
            left = mid + 1
        if less > len(arr1) - 1:
            right = mid - 1

    return left


def find_left_median_of_union(arrs):
    for i in range(len(arrs)):
        for j in range(i + 1, len(arrs)):
            print(count_left_median(arrs[i], arrs[j]))


n, l = map(int, input().split())
arrs = []

for _ in range(n):
    x1, d1, a, c, m = map(int, input().split())
    arr = [x1]
    prev_d = d1
    for i in range(1, l):
        x = arr[i - 1] + prev_d
        arr.append(x)
        prev_d = (a * prev_d + c) % m

    arrs.append(arr)

# n, l = 3, 6
# arrs = [[1, 4, 7, 10, 13, 16], [0, 2, 5, 9, 14, 20], [1, 7, 16, 16, 21, 22]]

find_left_median_of_union(arrs)
