def count_couples(distances, r):
    couples_count = 0
    right = 1
    for left in range(len(distances)):
        while right < len(distances) and distances[right] - distances[left] <= r:
            right += 1

        couples_count += len(distances) - right

    return couples_count


if __name__ == "__main__":
    n, r = map(int, input().split())
    distances = list(map(int, input().split()))

    # 2
    # r = 4
    # distances = [1, 3, 5, 8]

    print(count_couples(distances, r))
