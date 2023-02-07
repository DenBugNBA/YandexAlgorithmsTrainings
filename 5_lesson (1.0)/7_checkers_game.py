k = 2
nums = [1, 1, 2, 2, 3]  # 9

nums_count = {}
for num in nums:
    if num not in nums_count:
        nums_count[num] = 0
    nums_count[num] += 1

unique_nums = list(nums_count.keys())
unique_nums.sort()
# print(unique_nums, "- unique nums sorted")

right = 0
possible_scores_count = 0
duplicates = 0  # более 1 раза в промежутке от L+1 до R-1

for left in range(len(unique_nums)):
    while right < len(unique_nums) and unique_nums[left] * k >= unique_nums[right]:
        if nums_count[unique_nums[right]] >= 2:
            duplicates += 1
        right += 1

    range_len = right - left  # длина отрезка включая L

    if nums_count[unique_nums[left]] >= 2:  # Если в L больше двух
        possible_scores_count += (range_len - 1) * 3
    if nums_count[unique_nums[left]] >= 3:  # Если в L больше трёх
        possible_scores_count += 1

    possible_scores_count += (range_len - 1) * (range_len - 2) * 3

    if nums_count[unique_nums[left]] >= 2:
        duplicates -= 1

    possible_scores_count += duplicates * 3

print(possible_scores_count)
