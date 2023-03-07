def check_greater_or_equal(mid, arr, target):
    return arr[mid] >= target


def binary_search(left, right, check, params):
    target, arr = params

    while left < right:
        mid = (left + right) // 2
        if check(mid, arr, target):
            right = mid
        else:
            left = mid + 1

    if arr[left] != target:
        return -1
    return mid


def process_array(arr, nums_needed):
    arr = sorted(arr)

    for num in nums_needed:
        res = binary_search(0, len(arr) - 1, check_greater_or_equal, (num, arr))
        if res == -1:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    nums_needed = list(map(int, input().split()))

    # NO
    # YES
    # YES
    # YES
    # NO
    # NO
    # YES
    # YES
    # NO
    # YES
    # n, k = 10, 10
    # arr = [1, 61, 126, 217, 2876, 6127, 39162, 98126, 712687, 1000000000]
    # nums_needed = [100, 6127, 1, 61, 200, -10000, 1, 217, 10000, 1000000000]

    process_array(arr, nums_needed)
