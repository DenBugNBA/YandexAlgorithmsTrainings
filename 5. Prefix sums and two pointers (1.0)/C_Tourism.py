def count_prefix_sum(coords, direction):
    if direction == -1:
        coords = coords[::-1]

    prefix_sum_lifts = [0] * len(coords)

    prev_y = coords[0][1]

    for i in range(1, len(coords)):
        current_y = coords[i][1]

        if current_y > prev_y:
            prefix_sum_lifts[i] = prefix_sum_lifts[i - 1] + (current_y - prev_y)
        else:
            prefix_sum_lifts[i] = prefix_sum_lifts[i - 1]

        prev_y = current_y
        i += 1

    return prefix_sum_lifts


def count_height_of_lifts(prefix_sum_lifts, prefix_sum_lifts_rev, tracks):
    for s, f in tracks:
        if s <= f:
            print(prefix_sum_lifts[f - 1] - prefix_sum_lifts[s - 1])
        else:
            print(prefix_sum_lifts_rev[-f] - prefix_sum_lifts_rev[-s])


if __name__ == "__main__":
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))
    m = int(input())
    tracks = []
    for _ in range(m):
        s, f = map(int, input().split())
        tracks.append((s, f))

    # 4
    # coords = [(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)]
    # tracks = [(2, 6)]

    # 0
    # 5
    # 4
    # coords = [(1, 1), (3, 2), (5, 6), (7, 2), (10, 4), (11, 1)]
    # tracks = [(5, 6), (1, 4), (4, 2)]

    # 1
    # coords = [(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)]
    # tracks = [(3, 1)]

    prefix_sum_lifts = count_prefix_sum(coords, 1)
    prefix_sum_lifts_rev = count_prefix_sum(coords, -1)
    count_height_of_lifts(prefix_sum_lifts, prefix_sum_lifts_rev, tracks)
