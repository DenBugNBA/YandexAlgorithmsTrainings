"""
По последовательности чисел во входных данных определите ее вид:

CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов
"""


def determine_sequence_type(arr):
    if not arr:
        return "RANDOM"

    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            break
    else:
        return "CONSTANT"

    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            break
    else:
        return "DESCENDING"

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            break
    else:
        return "WEAKLY DESCENDING"

    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            break
    else:
        return "ASCENDING"

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            break
    else:
        return "WEAKLY ASCENDING"

    return "RANDOM"


if __name__ == "__main__":
    arr = []
    num = int(input())
    while num != -2000000000:
        arr.append(num)
        num = int(input())

    # CONSTANT
    # arr = [-530, -530, -530, -530, -530]

    # DESCENDING
    # arr = [5, 4, 3, 2, 1]

    # WEAKLY DESCENDING
    # arr = [5, 4, 4, 2, 1]

    # ASCENDING
    # arr = [1, 2, 3, 4, 5]

    # WEAKLY ASCENDING
    # arr = [1, 2, 3, 3, 5]

    #  RANDOM
    # arr = [1, 5, 3, 2, 4]

    # RANDOM
    # arr = []

    print(determine_sequence_type(arr))
