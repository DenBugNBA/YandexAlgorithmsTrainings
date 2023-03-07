def intersection_of_sets(arr1, arr2):
    return sorted((set(arr1) & set(arr2)))


if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # 2 3
    # arr1 = [1, 3, 2]
    # arr2 = [4, 3, 2]

    # 2 4
    # arr1 = [1, 2, 6, 4, 5, 7]
    # arr2 = [10, 2, 3, 4, 8]

    # 1 4
    # arr1 = [5, 4, 3, 2, 1]
    # arr2 = [4, 1]

    res = intersection_of_sets(arr1, arr2)
    print(*res)
