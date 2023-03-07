def merge_two_sequences(arr1, arr2):
    merged = [0] * (len(arr1) + len(arr2))
    first = second = 0

    for i in range(len(arr1) + len(arr2)):
        if first != len(arr1) and (second == len(arr2) or arr1[first] <= arr2[second]):
            merged[i] = arr1[first]
            first += 1
        else:
            merged[i] = arr2[second]
            second += 1

    return merged


arr1 = [1, 3, 5, 7]
arr2 = [3, 4, 4]

merged = merge_two_sequences(arr1, arr2)
print(merged)
