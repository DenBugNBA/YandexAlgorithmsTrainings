def sort_counting(arr):
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1

    count = [0] * k

    for num in arr:
        count[num - min_val] += 1

    current_index = 0
    for val in range(0, k):
        for _ in range(count[val]):
            arr[current_index] = val + min_val
            current_index += 1

    return arr


arr = [5, 3, 5, 3, 4, 5, 2, 1, 4]
print(sort_counting(arr))
