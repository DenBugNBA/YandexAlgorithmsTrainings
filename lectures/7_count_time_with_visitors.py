def count_time_with_visitors(n, times_in, times_out):
    events = []

    for i in range(n):
        events.append((times_in[i], -1))  # пришёл
        events.append((times_out[i], 1))  # ушёл
    events.sort()

    current_online = 0
    time_with_visitors = 0

    for i in range(len(events)):
        if current_online > 0:
            time_with_visitors += events[i][0] - events[i - 1][0]

        if events[i][1] == -1:
            current_online += 1
        else:
            current_online -= 1

    return time_with_visitors
