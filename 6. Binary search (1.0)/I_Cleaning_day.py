def check_possible_difference(difference, params):
    r, c, heights = params

    teams_count = 0

    left = 0
    for right in range(len(heights)):
        if right - left + 1 == c:
            if heights[right] - heights[left] <= difference:
                teams_count += 1
                left = right + 1
            else:
                left += 1

    return teams_count >= r


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right) // 2

        if check(mid, params):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    # n человек, r бригад по c человек в каждой
    n, r, c = map(int, input().split())
    heights = []
    for _ in range(n):
        heights.append(int(input()))

    # 30
    # n, r, c = 8, 2, 3
    # heights = [170, 205, 225, 190, 260, 130, 225, 160]

    heights = sorted(heights)

    max_difference = max(heights) - min(heights)

    print(binary_search(0, max_difference, check_possible_difference, (r, c, heights)))
