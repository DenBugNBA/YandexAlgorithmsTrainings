if __name__ == "__main__":
    n = int(input())

    events = [0] * (n * 2)

    for i in range(0, n * 2, 2):
        l, r = map(int, input().split())
        events[i] = (l, -1)
        events[i + 1] = (r, 1)
    events.sort()

    current_intervals = 0
    length_painted = 0

    for i in range(n * 2):
        if current_intervals > 0:
            length_painted += events[i][0] - events[i - 1][0]

        # начало отрезка
        if events[i][1] == -1:
            current_intervals += 1
        # конец отрезка
        elif events[i][1] == 1:
            current_intervals -= 1

    print(length_painted)
