def count_time_all_working(checkout):
    events = []
    checkouts_amount = 0

    for i in range(len(checkout)):
        open_hour, open_minute, close_hour, close_minute = checkout[i]
        if open_hour != close_hour or open_minute != close_minute:
            checkouts_amount += 1
            events.append((open_hour, open_minute, 1, i))
            events.append((close_hour, close_minute, -1, i))
    events.sort()

    if len(events) == 0:
        return 24 * 60

    current_opened = set()

    for i in range(len(events)):
        if events[i][2] == -1 and events[i][3] in current_opened:
            current_opened.remove(events[i][3])

        elif events[i][2] == 1:
            current_opened.add(events[i][3])

    time_all_working = 0

    for i in range(len(events)):
        if events[i][2] == -1:
            if len(current_opened) == checkouts_amount:
                hours = events[i][0] if i == 0 else events[i][0] - events[i - 1][0]
                minutes = events[i][1] if i == 0 else events[i][1] - events[i - 1][1]

                time_all_working += minutes + (hours * 60)

            current_opened.remove(events[i][3])

        elif events[i][2] == 1:
            current_opened.add(events[i][3])

    if len(current_opened) == checkouts_amount and events[len(events) - 1][2] == 1:
        hours = 24 - events[len(events) - 1][0]
        minutes = events[len(events) - 1][1]

        time_all_working += (hours * 60) - minutes

    return time_all_working


if __name__ == "__main__":
    n = int(input())
    checkout = []
    for _ in range(n):
        open_hour, open_minute, close_hour, close_minute = map(int, input().split())
        checkout.append((open_hour, open_minute, close_hour, close_minute))

    # 120
    # checkout = [(1, 0, 23, 0), (12, 0, 12, 0), (22, 0, 2, 0)]

    # 0
    # checkout = [(9, 30, 14, 0), (14, 15, 21, 0)]

    # 1
    # checkout = [(14, 0, 18, 0), (10, 0, 14, 1)]

    # 1440
    # checkout = [(14, 0, 14, 0), (11, 0, 11, 0)]

    # 241
    # checkout = [(14, 0, 14, 0), (10, 0, 14, 1)]

    # 12:59 - 14:52
    # 1 до 13:00, 60 с 13:00 до 14:00, 52 с 14:00 до 14:52 - 1 + 60 + 52 = 113
    # 113
    # checkout = [(10, 0, 14, 52), (12, 59, 14, 53)]

    # 1
    # checkout = [(23, 59, 0, 0)]

    print(count_time_all_working(checkout))
