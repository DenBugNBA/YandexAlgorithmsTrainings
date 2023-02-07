from itertools import permutations


def count_possible_scores(nums, k):
    possible_scores_count = 0

    sorted_nums = sorted(nums)

    right = 0
    left = 0
    prev_left_number = None
    prev_right_number = None
    while left < len(sorted_nums):
        while right < len(sorted_nums) and sorted_nums[right] / sorted_nums[left] <= k:
            right += 1

        if (
            (right - 1) - left + 1 >= 3
            and sorted_nums[right - 1] / sorted_nums[left] <= k
            and sorted_nums[left] != prev_left_number
            and sorted_nums[right - 1] != prev_right_number
        ):
            possible_scores_count += len(set(permutations(sorted_nums[left:right], 3)))

        prev_left_number = sorted_nums[left]
        prev_right_number = sorted_nums[right - 1]
        left += 1

    return possible_scores_count


# n, k = map(int, input().split())
# nums = list(map(int, input().split()))

k = 2
nums = [1, 1, 2, 2, 3]  # 9

# k = 2
# nums = [3, 2, 2, 1, 1]  # 9

# k = 3
# nums = [1, 2, 3]  # 6

# k = 3
# nums = [1, 1, 2, 2, 3]  # 18

# k = 2
# nums = [1, 10, 100]  # 0

# k = 2
# nums = [1, 10, 100, 101, 102]  # 6

# k = 5
# nums = [1, 2, 3, 4]  # 24

# k = 100
# nums = [1, 10, 100, 101, 102]  # 30

# k = 1
# nums = [5, 5, 5, 5, 5, 5]  # 1


print(count_possible_scores(nums, k))
