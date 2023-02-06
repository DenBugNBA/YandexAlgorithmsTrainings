def can_throw_away(a, b, c, d, e):
    brick = sorted([a, b, c])
    hole = sorted([d, e])

    if brick[0] <= hole[0] and brick[1] <= hole[1]:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    # YES
    # a = 1
    # b = 1
    # c = 1
    # d = 1
    # e = 1

    # NO
    # a = 2
    # b = 2
    # c = 2
    # d = 1
    # e = 1

    print(can_throw_away(a, b, c, d, e))
