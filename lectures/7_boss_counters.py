def boss_counters(n, times_in, times_out, m, times_boss):
    events = []

    for i in range(n):
        events.append((times_in[i], -1))
        events.append((times_out[i], 1))

    for i in range(m):
        events.append(times_boss[i], 0)

    events.sort()

    current_online = 0
    boss_result = []

    for event in events:
        if event[1] == -1:
            current_online += 1
        elif event[1] == 1:
            current_online -= 1
        else:
            boss_result.append(current_online)

    return boss_result
