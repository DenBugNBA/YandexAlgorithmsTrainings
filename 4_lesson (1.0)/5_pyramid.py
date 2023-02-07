n = int(input())
sizes = []
for _ in range(n):
    width, height = map(int, input().split())
    sizes.append((width, height))

# sizes = [(3, 1), (2, 2), (3, 3)]


def count_max_height(sizes):
    current_width = 0
    max_height = 0

    for width, height in sorted(sizes, reverse=True):
        if width != current_width:
            max_height += height
            current_width = width

    return max_height


print(count_max_height(sizes))
