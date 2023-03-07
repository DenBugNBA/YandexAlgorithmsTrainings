def find_shortest_segment(colors, k):
    current_colors = {}

    min_segment_length = len(colors) + 1
    result = [0, 0]

    right = 0
    for left in range(len(colors)):
        while right < len(colors) and len(current_colors.keys()) < k:
            color = colors[right]

            if color not in current_colors:
                current_colors[color] = 0
            current_colors[color] += 1

            right += 1

        if len(current_colors) == k:
            if right - left < min_segment_length:
                result = [left + 1, right]
                min_segment_length = right - left

        first_color = colors[left]
        current_colors[first_color] -= 1
        if current_colors[first_color] == 0:
            del current_colors[first_color]

    return result


if __name__ == "__main__":
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))

    # 2 4
    # k = 3
    # colors = [1, 2, 1, 3, 2]

    # 2 6
    # k = 4
    # colors = [2, 4, 2, 3, 3, 1]

    # 1 3
    # k = 3
    # colors = [1, 3, 2, 1]

    # 1 3
    # k = 3
    # colors = [1, 2, 3]

    res = find_shortest_segment(colors, k)
    print(*res)
