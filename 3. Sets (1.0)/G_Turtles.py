def count_truth(n, places):
    possible_places = [0] * n

    for ahead, behind in places:
        if ahead + behind <= n - 1 and ahead >= 0 and behind >= 0:
            if possible_places[ahead] == 0 and n - ahead - 1 == behind:
                possible_places[ahead] = 1

    return possible_places.count(1)


if __name__ == "__main__":
    n = int(input())
    places = []
    for _ in range(n):
        x, y = map(int, input().split())
        places.append((x, y))

    # 2
    # n = 3
    # places = [(2, 0), (0, 2), (2, 2)]

    # 5
    # n = 5
    # places = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]

    # 4
    # n = 10
    # places = [
    #     (9, 1),
    #     (8, 1),
    #     (7, 2),
    #     (6, 2),
    #     (5, 3),
    #     (4, 4),
    #     (3, 6),
    #     (2, 7),
    #     (1, 9),
    #     (0, 8),
    # ]

    # 1
    # n = 1
    # places = [(0, 0)]

    print(count_truth(n, places))
