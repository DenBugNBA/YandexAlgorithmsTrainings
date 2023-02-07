arr = list(map(int, input().split()))

# arr = [1, 2, 3, 4, 5]
# arr = [5, 4, 3, 2, 1]
# arr = [1, 5, 1, 5, 1]


def count_bigger_neighbors(arr):
    count = 0

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1

    return count


print(count_bigger_neighbors(arr))
