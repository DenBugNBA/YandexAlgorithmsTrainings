def find_two_closest_nums(nums1, nums2):
    res = [0, 0]
    min_diff = nums2[len(nums2) - 1]

    first = 0
    second = 0

    for _ in range(len(nums1) + len(nums2)):
        current_diff = abs(nums1[first] - nums2[second])
        if current_diff < min_diff:
            res = [first, second]
            min_diff = current_diff

        if first != len(nums1) - 1 and nums1[first] < nums2[second]:
            first += 1
        elif second != len(nums2) - 1 and nums2[second] < nums1[first]:
            second += 1
        else:
            break

    return nums1[res[0]], nums2[res[1]]


# n = int(input())
# nums1 = list(map(int, input().split()))
# m = int(input())
# nums2 = list(map(int, input().split()))

# n = 2
# nums1 = [3, 4]
# m = 3
# nums2 = [1, 2, 3]

# n = 2
# nums1 = [4, 5]
# m = 3
# nums2 = [1, 2, 3]

# n = 5
# nums1 = [1, 2, 3, 4, 5]
# m = 5
# nums2 = [1, 2, 3, 4, 5]

n = 5
nums1 = [1, 2, 3, 4, 9, 10]
m = 5
nums2 = [5, 6, 7, 8, 13, 14]

result = find_two_closest_nums(nums1, nums2)
print(*result)
