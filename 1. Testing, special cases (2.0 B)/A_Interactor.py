def define_verdict(r, i, c):
    if i == 0:
        if r != 0:
            return 3
        else:
            return c
    elif i == 1:
        return c
    elif i == 4:
        if r != 0:
            return 3
        else:
            return 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    else:
        return i


if __name__ == "__main__":
    r = int(input())  # -128 ... 127
    i = int(input())  # 0 ... 7
    c = int(input())  # 0 ... 7

    # 0
    # r = 0
    # i = 0
    # c = 0

    # 3
    # r = -1
    # i = 0
    # c = 1

    # 6
    # r = 42
    # i = 1
    # c = 6

    # 1
    # r = 44
    # i = 7
    # c = 4

    # 3
    # r = 1
    # i = 4
    # c = 0

    # 2
    # r = -3
    # i = 2
    # c = 4

    print(define_verdict(r, i, c))
