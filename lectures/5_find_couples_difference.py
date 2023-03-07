def count_couples_difference(nums, k):
    # count b - a > k
    couples_count = 0

    right = 0
    for left in range(len(nums)):
        while right < len(nums) and nums[right] - nums[left] <= k:
            right += 1
        couples_count += len(nums) - right
    return couples_count


# sorted arr
nums = [1, 3, 5, 7, 8]
k = 4
print(count_couples_difference(nums, k))
