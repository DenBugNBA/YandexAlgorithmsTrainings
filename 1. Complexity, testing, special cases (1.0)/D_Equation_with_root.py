"""
    sqrt(ax + b) = c
    ax + b = c^2
    x = (c^2 - b) / a
"""


def solve_equation_with_root(a, b, c):
    if c < 0:
        return "NO SOLUTION"
    if a == 0:
        if b == 0 and c == 0:
            return "MANY SOLUTIONS"
        if c**2 == b:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"

    solution = (c**2 - b) / a

    if solution == int(solution):
        return int(solution)
    else:
        return "NO SOLUTION"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    # 0
    # a = 1
    # b = 0
    # c = 0

    # 7
    # a = 1
    # b = 2
    # c = 3

    # NO SOLUTION
    # a = 1
    # b = 2
    # c = -3

    # NO SOLUTION
    # a = 0
    # b = 15
    # c = 4

    print(solve_equation_with_root(a, b, c))
