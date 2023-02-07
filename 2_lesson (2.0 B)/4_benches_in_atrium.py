l, k = map(int, input().split())
positions = list(map(int, input().split()))

# l, k = 1, 1
# positions = [0] # 0

# l, k = 2, 2
# positions = [0, 1]

mid = l / 2
# print(mid)

left = 0
right = 0

for position in positions:
    if position < mid:
        left = position
    if position + 1 > mid:
        right = position
        break

if left != right:
    print(left, right)
else:
    print(left)
