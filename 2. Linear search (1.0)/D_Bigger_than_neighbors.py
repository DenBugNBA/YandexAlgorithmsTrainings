def count_bigger_neighbors(arr):
    count = 0

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    return count


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    # 0
    # arr = [1, 2, 3, 4, 5]

    # 0
    # arr = [5, 4, 3, 2, 1]

    # 2
    # arr = [1, 5, 1, 5, 1]

    print(count_bigger_neighbors(arr))
