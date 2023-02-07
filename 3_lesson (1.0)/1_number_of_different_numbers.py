# nums = list(map(int, input().split()))

# nums = [1, 2, 3, 2, 1]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]


def count_unique(arr):
    return len(set(arr))


print(count_unique(nums))
