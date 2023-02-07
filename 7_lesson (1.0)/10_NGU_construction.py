def count_minimum_blocks(n, w, l, coordinates):
    events = []

    for i in range(len(coordinates)):
        x1, y1, z1, x2, y2, z2 = coordinates[i]

        block_square = (y2 - y1) * (x2 - x1)

        events.append((z1, 1, block_square, i + 1))
        events.append((z2, -1, block_square, i + 1))
    events.sort()

    total_square = w * l
    current_square = 0

    current_blocks = 0
    min_blocks = n + 1

    for i in range(len(events)):
        _, event_id, block_square, _ = events[i]

        # конец блока по координате z
        if event_id == -1:
            current_blocks -= 1
            current_square -= block_square

        # начало блока по координате z
        if event_id == 1:
            current_blocks += 1
            current_square += block_square

        if current_square == total_square and current_blocks < min_blocks:
            min_blocks = current_blocks

    if min_blocks == n + 1:
        print("NO")
    else:
        current_blocks = 0
        current_square = 0

        block_numbers = set()

        for i in range(len(events)):
            _, event_id, block_square, block_number = events[i]

            # конец блока по координате z
            if event_id == -1:
                current_blocks -= 1
                current_square -= block_square
                block_numbers.remove(block_number)

            # начало блока по координате z
            if event_id == 1:
                current_blocks += 1
                current_square += block_square
                block_numbers.add(block_number)

            if current_square == total_square and current_blocks == min_blocks:
                print("YES")
                print(min_blocks)
                for num in list(block_numbers):
                    print(num)
                break

    return


n, w, l = map(int, input().split())
coordinates = []
for _ in range(n):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    coordinates.append((x1, y1, z1, x2, y2, z2))

# print(coordinates)

# YES
# 1
# 1
# n, w, l = 1, 10, 10
# coordinates = [(0, 0, 0, 10, 10, 10)]

# NO
# n, w, l = 2, 10, 10
# coordinates = [(0, 0, 0, 10, 5, 5), (0, 5, 5, 10, 10, 10)]

# YES
# 2
# 1
# 2
# n, w, l = 2, 10, 10
# coordinates = [(0, 0, 6, 5, 10, 7), (5, 0, 5, 10, 10, 10)]

# YES
# 2
# 1
# 3
# n, w, l = 3, 10, 10
# coordinates = [(0, 0, 6, 5, 10, 7), (0, 5, 1, 5, 10, 6), (5, 0, 5, 10, 10, 8)]

# NO
# n, w, l = 2, 10, 10
# coordinates = [(0, 0, 6, 5, 10, 7), (5, 0, 5, 9, 10, 8)]

count_minimum_blocks(n, w, l, coordinates)
