# arr = list(map(int, input().split()))

# arr = [1, 7, 9]
# arr = [1, 9, 7]
arr = [2, 2, 2]


def is_increasing_list(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return "NO"

    return "YES"


print(is_increasing_list(arr))
