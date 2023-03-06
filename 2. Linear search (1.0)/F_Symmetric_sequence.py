def make_symmetric(arr):
    n = len(arr)

    count = 0

    i = 0
    while arr != arr[::-1]:
        count += 1
        arr.insert(n, arr[i])
        i += 1

    return count, arr[n:]


if __name__ == "__main__":
    n = input()
    arr = list(map(int, input().split()))

    # 0
    # arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]

    # 3
    # 1 2 1
    # arr = [1, 2, 1, 2, 2]

    # 4
    # 4 3 2 1
    # arr = [1, 2, 3, 4, 5]

    # 1
    # 1
    # arr = [1, 5, 5, 5, 5, 5, 5]

    result = make_symmetric(arr)
    if len(result[1]) == 0:
        print(result[0])
    else:
        print(result[0])
        print(*result[1])
