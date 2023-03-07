if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # 2
    # arr1 = [1, 3, 2]
    # arr2 = [4, 3, 2]

    # 2
    # arr1 = [1, 2, 6, 4, 5, 7]
    # arr2 = [10, 2, 3, 4, 8]

    # 5
    # arr1 = [1, 7, 3, 8, 10, 2, 5]
    # arr2 = [6, 5, 2, 8, 4, 3, 7]

    print(len(set(arr1) & set(arr2)))
