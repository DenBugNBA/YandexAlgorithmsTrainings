def make_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    return prefix_sum


# [L, R)
def range_sum_query(prefix_sum, left, right):
    return prefix_sum[right] - prefix_sum[left]


nums = [5, 3, 8, 1, 4, 6]
prefix_sum = make_prefix_sum(nums)
print(prefix_sum)
print(range_sum_query(prefix_sum, 0, 2))  # 5 + 3 = 8
print(range_sum_query(prefix_sum, 2, 5))  # 8 + 1 + 4 = 13
