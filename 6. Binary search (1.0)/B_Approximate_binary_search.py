def check_less_or_equal(mid, arr, target):
    return arr[mid] <= target


def binary_search(left, right, check, params):
    target, arr = params

    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, arr, target):
            left = mid
        else:
            right = mid - 1

    return left


def process_array(arr, nums_needed):
    for num in nums_needed:
        index = binary_search(0, len(arr) - 1, check_less_or_equal, (num, arr))

        if index < len(arr) - 1 and abs(num - arr[index + 1]) < abs(num - arr[index]):
            print(arr[index + 1])
        else:
            print(arr[index])


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    nums_needed = list(map(int, input().split()))

    # 1
    # 3
    # 7
    # 1
    # 5
    # n, k = 10, 10
    # arr = [1, 3, 5, 7, 9]
    # nums_needed = [2, 4, 8, 1, 6]

    process_array(arr, nums_needed)
