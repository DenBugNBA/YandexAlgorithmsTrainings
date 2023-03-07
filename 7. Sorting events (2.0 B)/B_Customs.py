if __name__ == "__main__":
    n = int(input())

    events = [0] * (n * 2)

    for i in range(0, n * 2, 2):
        t, l = map(int, input().split())
        events[i] = (t, 1)
        events[i + 1] = (t + l, -1)
    events.sort()

    max_devices = 0
    current_devices = 0

    for event in events:
        # аппарат освобождатеся
        if event[1] == -1:
            current_devices -= 1

        # аппарат начинает досмотр
        elif event[1] == 1:
            current_devices += 1
            max_devices = max(max_devices, current_devices)

    print(max_devices)
