def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b > c:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    # YES
    # a = 4
    # b = 5
    # c = 3

    # YES
    # a = 3
    # b = 5
    # c = 4

    # YES
    # a = 3
    # b = 4
    # c = 5

    print(is_triangle(a, b, c))
