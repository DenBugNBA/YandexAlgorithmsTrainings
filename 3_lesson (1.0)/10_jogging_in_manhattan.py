def extend(rectangle, d):
    minPlus, maxPlus, minMinus, maxMinus = rectangle
    return [minPlus - d, maxPlus + d, minMinus - d, maxMinus + d]


def intersect(rect1, rect2):
    ans = [
        max(rect1[0], rect2[0]),
        min(rect1[1], rect2[1]),
        max(rect1[2], rect2[2]),
        min(rect1[3], rect2[3]),
    ]
    return ans


t, d, n = map(int, input().split())
pos_rectangle = (0, 0, 0, 0)  # прямоугольник после текущего шага
for _ in range(n):
    pos_rectangle = extend(pos_rectangle, t)
    navX, navY = map(int, input().split())
    nav_rectangle = extend((navX + navY, navX + navY, navX - navY, navX - navY), d)
    pos_rectangle = intersect(pos_rectangle, nav_rectangle)

points = []
for x_plus_y in range(pos_rectangle[0], pos_rectangle[1] + 1):
    for x_minus_y in range(pos_rectangle[2], pos_rectangle[3] + 1):
        if (x_plus_y + x_minus_y) % 2 == 0:
            x = (x_plus_y + x_minus_y) // 2
            y = x_plus_y - x
            points.append((x, y))

print(len(points))
for point in points:
    print(*point)
