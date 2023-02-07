"""
Математическая часть - векторное и псевдоскалярное произведения.
Реализация - считаются произведения (1, 2, 3 - вершины треугольника, 0 - точка):
(x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
(x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
(x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
Если они одинакового знака, то точка внутри треугольника, если что-то из этого - ноль,
то точка лежит на стороне, иначе точка вне треугольника.
"""


def determine_relative_location(d, x_point, y_point):
    a = (0, 0)
    b = (d, 0)
    c = (0, d)

    product1 = (a[0] - x_point) * (b[1] - a[1]) - (b[0] - a[0]) * (a[1] - y_point)
    product2 = (b[0] - x_point) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - y_point)
    product3 = (c[0] - x_point) * (a[1] - c[1]) - (a[0] - c[0]) * (c[1] - y_point)

    if (
        (product1 > 0 and product2 > 0 and product3 > 0)
        or (product1 < 0 and product2 < 0 and product3 < 0)
        or product1 == 0
        or product2 == 0
        or product3 == 0
    ):
        return 0
    else:
        a_distance = ((a[0] - x_point) ** 2 + (a[1] - y_point) ** 2) ** (1 / 2)
        b_distance = ((b[0] - x_point) ** 2 + (b[1] - y_point) ** 2) ** (1 / 2)
        c_distance = ((c[0] - x_point) ** 2 + (c[1] - y_point) ** 2) ** (1 / 2)

        if a_distance <= b_distance and a_distance <= c_distance:
            return 1
        elif b_distance <= a_distance and b_distance <= c_distance:
            return 2
        else:
            return 3


if __name__ == "__main__":
    d = int(input())
    x_point, y_point = map(int, input().split())

    # 0
    # d = 5
    # x_point, y_point = 1, 1

    # 1
    # d = 3
    # x_point, y_point = -1, -1

    # 2
    # d = 4
    # x_point, y_point = 4, 4

    # 0
    # d = 4
    # x_point, y_point = 2, 2

    print(determine_relative_location(d, x_point, y_point))
