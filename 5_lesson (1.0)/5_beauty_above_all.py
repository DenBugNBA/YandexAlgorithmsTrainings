def find_shortest_segment(colors, k):
    current_colors = {}

    min_segment_length = len(colors) + 1
    result = [0, 0]

    right = 0
    for left in range(len(colors)):
        # print(left, "- left")
        while right < len(colors) and len(current_colors.keys()) < k:
            color = colors[right]

            if color not in current_colors:
                current_colors[color] = 0
            current_colors[color] += 1

            right += 1

        # print(len(current_colors))

        if len(current_colors) == k:
            if right - left < min_segment_length:
                # print(right, left)
                result = [left + 1, right]
                min_segment_length = right - left

        first_color = colors[left]
        current_colors[first_color] -= 1
        if current_colors[first_color] == 0:
            del current_colors[first_color]

    return result


# n, k = map(int, input().split())
# colors = list(map(int, input().split()))

k = 3
colors = [1, 2, 1, 3, 2]

# k = 4
# colors = [2, 4, 2, 3, 3, 1]

# k = 3
# colors = [1, 3, 2, 1]

# k = 3
# colors = [1, 2, 3]

res = find_shortest_segment(colors, k)
print(*res)
