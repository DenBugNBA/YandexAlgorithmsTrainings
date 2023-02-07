def count_sum_of_numbers(nums, k):
    amount_of_ways = 0
    current_sum = 0

    second = 0
    for first in range(len(nums)):
        while second != len(nums) and current_sum < k:
            current_sum += nums[second]
            second += 1

        if current_sum == k:
            amount_of_ways += 1

        current_sum -= nums[first]

    return amount_of_ways


# n, k = map(int, input().split())
# nums = list(map(int, input().split()))

k = 17
nums = [17, 7, 10, 7, 10]  # 4

# k = 10
# nums = [1, 2, 3, 4, 1]  # 2

# k = 3
# nums = [2, 1, 1, 2]  # 2

# k = 11
# nums = [6, 6, 3, 1, 11]  # 1

# k = 11
# nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]  # 1

# k = 4
# nums = [1, 1, 3, 1, 3]  # 3

print(count_sum_of_numbers(nums, k))
