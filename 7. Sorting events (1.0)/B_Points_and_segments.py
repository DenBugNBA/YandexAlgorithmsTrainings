def count_amount_of_segments_for_point(points, segments):
    events = []

    for i in range(len(segments)):
        a, b = segments[i]
        segment_from = min(a, b)
        segment_to = max(a, b)
        events.append((segment_from, -1))
        events.append((segment_to, 1))

    for i in range(len(points)):
        events.append((points[i], 0, i))

    events.sort()

    current_segments = 0
    segments_for_point = [0] * len(points)

    for event in events:
        if event[1] == -1:
            current_segments += 1
        elif event[1] == 1:
            current_segments -= 1
        else:
            index_of_point = event[2]
            segments_for_point[index_of_point] = current_segments

    return segments_for_point


if __name__ == "__main__":
    # n - число отрезков, m - число точек
    n, m = map(int, input().split())
    segments = []
    for i in range(n):
        a, b = map(int, input().split())
        segments.append((a, b))
    points = tuple(map(int, input().split()))

    # 2 0
    # segments = [(0, 5), (-3, 2), (7, 10)]
    # points = (1, 6)

    # 2 0
    # segments = [(5, 5), (-10, 5)]
    # points = (5, 6)

    res = count_amount_of_segments_for_point(points, segments)
    print(*res)
