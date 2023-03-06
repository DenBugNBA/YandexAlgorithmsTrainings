def find_closest_number(arr, x):
    closest = arr[0]
    min_difference = abs(x - closest)

    for i in range(1, len(arr)):
        difference = abs(x - arr[i])

        if difference < min_difference:
            min_difference = difference
            closest = arr[i]

    return closest


if __name__ == "__main__":
    n = input()
    arr = list(map(int, input().split()))
    x = int(input())

    # 5
    # arr = [1, 2, 3, 4, 5]
    # x = 6

    # 3
    # arr = [5, 4, 3, 2, 1]
    # x = 3

    print(find_closest_number(arr, x))
