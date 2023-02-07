# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

arr1 = [1, 3, 2]
arr2 = [4, 3, 2]

# arr1 = [1, 2, 6, 4, 5, 7]
# arr2 = [10, 2, 3, 4, 8]

# arr1 = [5, 4, 3, 2, 1]
# arr2 = [4, 1]


def intersection_of_sets(arr1, arr2):
    return sorted(list(set(arr1) & set(arr2)))


res = intersection_of_sets(arr1, arr2)
print(*res)
