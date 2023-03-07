def count_sum_of_marks(twos, threes, fours, fives):
    return twos * 2 + threes * 3 + fours * 4 + fives * 5


def check_average_mark(fives, params):
    twos, threes, fours = params

    sum_of_marks = count_sum_of_marks(twos, threes, fours, fives)
    marks_amount = sum((twos, threes, fours, fives))

    return sum_of_marks >= marks_amount * 3.5


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right) // 2

        if check(mid, params):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    # 2
    # a = 2
    # b = 0
    # c = 0

    print(binary_search(0, 10**30, check_average_mark, (a, b, c)))
