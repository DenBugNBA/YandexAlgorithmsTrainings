def count_max_users_online(n, times_in, times_out):
    events = []

    for i in range(n):
        events.append((times_in[i], -1))  # пришёл
        events.append((times_out[i], 1))  # ушёл
    events.sort()

    current_online = 0
    max_online = 0

    for event in events:
        if event[1] == -1:
            current_online += 1
        else:
            current_online -= 1
        max_online = max(max_online, current_online)

    return max_online
