# arr = list(map(int, input().split()))

# text = "12288 -10075 29710 15686 -18900 -17715 15992 24431"
# arr = list(map(int, text.split()))

# arr = [4, 3, 5, 2, 5]
# arr = [-4, 3, -5, 2, 5]
arr = [1, -1]


def find_two_maximums(arr):

    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

    return max1, max2


def max_product_of_two(arr):
    if len(arr) == 2:
        return min(arr), max(arr)

    positive = []
    negative = []

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(abs(num))

    max1 = max2 = max_neg1 = max_neg2 = 0
    if len(positive) > 1:
        max1, max2 = find_two_maximums(positive)
    if len(negative) > 1:
        max_neg1, max_neg2 = find_two_maximums(negative)

    if max1 * max2 > max_neg1 * max_neg2:
        return max2, max1
    else:
        return -max_neg1, -max_neg2


result = max_product_of_two(arr)
nums_string = " ".join(map(str, result))
print(nums_string)
