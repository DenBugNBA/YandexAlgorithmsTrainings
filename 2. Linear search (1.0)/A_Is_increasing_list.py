def is_increasing_list(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return "NO"

    return "YES"


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    # YES
    # arr = [1, 7, 9]

    # NO
    # arr = [1, 9, 7]

    # NO
    # arr = [2, 2, 2]

    print(is_increasing_list(arr))
