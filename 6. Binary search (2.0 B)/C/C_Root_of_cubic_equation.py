def check_greater_equal_zero(num, params):
    a, b, c, d = params
    expression = a * num**3 + b * num**2 + c * num + d
    # print(expression, "- expression")
    if a < 0:
        return expression <= 0
    return expression >= 0


def binary_search(left, right, eps, check, params):
    # print(left, right)
    while left + eps < right:
        m = (left + right) / 2
        if check(m, params):
            right = m
        else:
            left = m + eps
        # print(left, right)
    return left


def find_root_of_equation(a, b, c, d):
    eps = 0.00001

    return binary_search(
        -(10**5), 10**5, eps, check_greater_equal_zero, (a, b, c, d)
    )


if __name__ == "__main__":
    with open("cubroot.in") as f:
        line = f.readline()
    a, b, c, d = map(int, line.split())

    print(find_root_of_equation(a, b, c, d))
