def count_zero_segments(nums):
    prefix_sum_values = {
        0: 1,
    }

    zero_segments_count = 0
    current_sum = 0

    for num in nums:
        current_sum += num
        print(current_sum)
        if current_sum not in prefix_sum_values:
            prefix_sum_values[current_sum] = 0
        else:
            zero_segments_count += prefix_sum_values[current_sum]

        prefix_sum_values[current_sum] += 1

    return zero_segments_count


nums = [2, 3, -5, 3, 0, 2, -2]
zero_segments_count = count_zero_segments(nums)
print(zero_segments_count)
