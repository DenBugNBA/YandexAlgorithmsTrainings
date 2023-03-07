if __name__ == "__main__":
    l, k = map(int, input().split())
    positions = list(map(int, input().split()))

    # 2
    # l, k = 5, 2
    # positions = [0, 2]

    # 4 8
    # l, k = 13, 4
    # positions = [1, 4, 8, 11]

    # 6 8
    # l, k = 14, 6
    # positions = [1, 6, 8, 11, 12, 13]

    # 0
    # l, k = 1, 1
    # positions = [0]

    # 0 1
    # l, k = 2, 2
    # positions = [0, 1]

    mid = l / 2

    left = 0
    right = 0

    for position in positions:
        if position < mid:
            left = position
        if position + 1 > mid:
            right = position
            break

    if left != right:
        print(left, right)
    else:
        print(left)
