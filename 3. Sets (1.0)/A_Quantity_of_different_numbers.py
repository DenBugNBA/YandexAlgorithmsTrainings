def count_unique(arr):
    return len(set(arr))


if __name__ == "__main__":
    nums = list(map(int, input().split()))

    # 3
    # nums = [1, 2, 3, 2, 1]

    # 10
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 6
    # nums = [1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]

    print(count_unique(nums))
