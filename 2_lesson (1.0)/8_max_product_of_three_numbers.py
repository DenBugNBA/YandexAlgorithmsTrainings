import random

# arr = list(map(int, input().split()))

# text = "12288 -10075 29710 15686 -18900 -17715 15992 24431"
# arr = list(map(int, text.split()))

# arr = [4, 3, 5, 2, 5]
# arr = [-4, 3, -5, 2, 5]
# arr = [1, -1, 1]
arr = [3, 5, 1, 7, 9, 0, 9, -3, 10]
# arr = [-5, -30000, -12]
# arr = [1, 2, 3]
# arr = [4, -7, -4, 0, 10, 9, -7, -1]


def find_two_minimums(arr):

    min1 = min(arr[0], arr[1])
    min2 = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return min1, min2


def sort_two_nums(a, b):
    if a > b:
        return a, b
    return b, a


def find_three_maximums(arr):
    max1, max2, max3 = arr[0], arr[1], arr[2]
    max1, max2 = sort_two_nums(max1, max2)
    max1, max3 = sort_two_nums(max1, max3)
    max2, max3 = sort_two_nums(max2, max3)

    for i in range(3, len(arr)):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3:
            max3 = arr[i]

    return max1, max2, max3


def max_product_of_three(arr):
    if len(arr) <= 3:
        return arr

    positive = []
    negative = []

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

    max1 = max2 = max3 = None
    min_neg1 = min_neg2 = None

    # 3 max pos fill
    if len(positive) > 2:
        max1, max2, max3 = find_three_maximums(arr)
    # 2 min neg fill
    if len(negative) > 1:
        min_neg1, min_neg2 = find_two_minimums(negative)

    # (3 pos) or (2 neg 1 pos)
    if len(positive) > 2 and len(negative) > 1:
        if max1 * max2 * max3 > min_neg1 * min_neg2 * max1:
            return max1, max2, max3
        else:
            return min_neg1, min_neg2, max1

    # (3 pos)
    elif len(positive) > 2:
        return max1, max2, max3

    # 2 neg 1 pos
    elif len(negative) > 1 and len(positive) > 0:
        max1 = max(positive)
        return min_neg1, min_neg2, max1

    else:
        # 3 neg
        max_neg1, max_neg2, max_neg3 = find_three_maximums(negative)
        return max_neg1, max_neg2, max_neg3


def max_product_of_three_short(arr):
    if len(arr) <= 3:
        return arr

    max1, max2, max3 = find_three_maximums(arr)
    min1, min2 = find_two_minimums(arr)

    if max1 * max2 * max3 > min1 * min2 * max1:
        return max1, max2, max3
    else:
        return min1, min2, max1


result = max_product_of_three_short(arr)
nums_string = " ".join(map(str, result))
print(nums_string)


def correct(arr):
    if len(arr) <= 3:
        return arr

    nmax1 = arr[0]
    nmin1 = arr[0]

    for n in arr:
        if n > nmax1:
            nmax1 = n
        if n < nmin1:
            nmin1 = n

    arr.remove(nmax1)
    arr.remove(nmin1)
    nmax2 = arr[0]
    nmin2 = arr[0]

    for n in arr:
        if n > nmax2:
            nmax2 = n
        if n < nmin2:
            nmin2 = n

    arr.remove(nmax2)

    nmax3 = arr[0]

    for n in arr:
        if n > nmax3:
            nmax3 = n

    p1 = nmin1 * nmin2 * nmax1
    p2 = nmax1 * nmax2 * nmax3

    if p1 > p2:
        return (nmin1, nmin2, nmax1)
    else:
        return (nmax1, nmax2, nmax3)


def generate_arr():
    n = random.randint(3, 10)
    arr = []

    for _ in range(n):
        arr.append(random.randint(-10, 10))

    return arr


def stress_test():
    arr = generate_arr()
    print(arr)
    res_my = max_product_of_three(arr)
    res_correct = correct(arr)
    print("my:")
    print(res_my)
    print("correct:")
    print(res_correct)


# stress_test()
