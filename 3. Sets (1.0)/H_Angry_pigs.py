def count_min_shots(coordinates):
    x_coords = set()
    for x, _ in coordinates:
        x_coords.add(x)
    return len(x_coords)


if __name__ == "__main__":
    n = int(input())
    coordinates = []
    for _ in range(n):
        x, y = map(int, input().split())
        coordinates.append((x, y))

    # 3
    # coordinates = [(1, 1), (2, 2), (3, 3), (2, 1), (3, 2), (3, 1)]

    # 3
    # coordinates = [(1, 1), (2, 2), (3, 3), (2, 1), (3, 2), (3, 4)]

    print(count_min_shots(coordinates))
