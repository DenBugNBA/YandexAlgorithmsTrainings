# # n = int(input())
# points = n * []

# for _ in range(n):
#     x, y = map(int, input().split())
#     points.append(x, y)

n = 4
points = [(0, 0), (1, 1), (1, 0), (0, 1)]

result = 0  # троек вершин равнобедренных треугольников

for i in range(n):
    used_vectors = set()
    neighbors = []

    for j in range(n):
        vec_x = points[i][0] - points[j][0]
        vec_y = points[i][1] - points[j][1]
        vec_len = vec_x**2 + vec_y**2

        neighbors.append(vec_len)

        if (vec_x, vec_y) in used_vectors:
            result -= 1

        used_vectors.add((-vec_x, -vec_y))

    neighbors.sort()

    right = 0
    for left in range(len(neighbors)):
        while right < len(neighbors) and neighbors[left] == neighbors[right]:
            right += 1
        result += right - left - 1

print(result)
