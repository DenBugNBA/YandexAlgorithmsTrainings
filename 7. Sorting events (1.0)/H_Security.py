def is_secured_any_time(pairs):
    events = []

    for i in range(0, len(pairs), 2):
        interval_start = pairs[i]
        interval_end = pairs[i + 1]

        if interval_start != interval_end:
            events.append((interval_end, -1, i))
            events.append((interval_start, 1, i))
    events.sort()

    if events[0][0] != 0 or events[-1][0] != 10000:
        return False

    current_securities = 0

    for i in range(len(events)):
        # уход охранника
        if events[i][1] == -1:
            # если пришло 2 охранника и последний пришедший ушёл первым
            if current_securities == 2 and events[i - 1][2] == events[i][2]:
                return False

            # если 2 охранника ушли одновременно
            if events[i - 1][1] == -1 and events[i - 1][0] == events[i][0]:
                return False

            current_securities -= 1

        # приход охранника
        elif events[i][1] == 1:
            # если пришло 3 подряд
            if current_securities == 2:
                return False

            # если 2 пришли в одно время
            if i != 0 and events[i - 1][0] == events[i][0] and events[i - 1][1] == 1:
                return False

            # если есть промежутки без охраны
            if i != 0 and current_securities == 0 and events[i - 1][0] != events[i][0]:
                return False

            current_securities += 1

    return True


if __name__ == "__main__":
    k = int(input())
    for _ in range(k):
        _, *pairs = map(int, input().split())

        if is_secured_any_time(pairs):
            print("Accepted")
        else:
            print("Wrong Answer")

# Wrong Answer
# Accepted
"""
2
3 0 3000 2500 7000 2700 10000
2 0 3000 2700 10000
"""
