# n = input()
# arr = list(map(int, input().split()))

arr = [10, 20, 15, 10, 30, 5, 1]
# arr = [15, 15, 10]
# arr = [10, 15, 20]


def max_place(arr):
    index_max = 0
    max_distance = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_distance:
            max_distance = arr[i]
            index_max = i

    index_participant = -1
    max_participant = -1

    for i in range(index_max + 1, len(arr) - 1):
        if arr[i] > max_participant and str(arr[i])[-1] == "5" and arr[i + 1] < arr[i]:
            max_participant = arr[i]
            index_participant = i

    if max_participant == -1:
        return 0

    place = 1

    for i in range(0, index_participant):
        if arr[i] > max_participant:
            place += 1
    for i in range(index_participant + 1, len(arr)):
        if arr[i] > max_participant:
            place += 1

    return place


print(max_place(arr))
