num = -1
max_num = 0
nums = []

while num != 0:
    num = int(input())

    if num > max_num:
        max_num = num

    nums.append(num)

max_count = 0

for num in nums[:-1]:
    if num == max_num:
        max_count += 1

print(max_count)
