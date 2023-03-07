def make_prefix_zeroes(nums):
    prefix_zeroes = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefix_zeroes[i] = prefix_zeroes[i - 1] + 1
        else:
            prefix_zeroes[i] = prefix_zeroes[i - 1]

    return prefix_zeroes


# [L, R)
def count_zeroes(prefix_zeroes, left, right):
    return prefix_zeroes[right] - prefix_zeroes[left]


nums = [1, 2, 0, 0, 1, 3, 0, 4]
prefix_zeroes = make_prefix_zeroes(nums)
print(prefix_zeroes)
print(count_zeroes(prefix_zeroes, 0, 2))
print(count_zeroes(prefix_zeroes, 2, 5))
print(count_zeroes(prefix_zeroes, 0, 7))
