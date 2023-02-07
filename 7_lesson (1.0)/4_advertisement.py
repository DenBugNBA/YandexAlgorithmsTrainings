def find_two_times_for_advertisement(customers):
    events = []

    for i in range(len(customers)):
        time_in, time_out = customers[i]
        if time_out - time_in >= 5:
            events.append((time_in, -1, i))
            events.append((time_out, 1, i))
    events.sort()

    if len(events) == 0:
        return (0, 10, 20)

    elif len(events) == 2:
        return (1, events[0][0], events[0][0] + 10)

    else:
        max_heard = 0
        first_best, second_best = 0, 0
        first_heard = set()

        for i in range(len(events)):
            event1 = events[i]

            if event1[1] == -1:
                first_heard.add(event1[2])

                if len(first_heard) > max_heard:
                    max_heard = len(first_heard)
                    first_best = event1[0]
                    second_best = event1[0] + 5

            second_heard = 0

            for j in range(i + 1, len(events)):
                event2 = events[j]
                if event2[1] == -1 and event2[2] not in first_heard:
                    second_heard += 1
                if (
                    event2[0] - 5 >= event1[0]
                    and len(first_heard) + second_heard > max_heard
                ):
                    max_heard = len(first_heard) + second_heard
                    first_best = event1[0]
                    second_best = event2[0]
                if event2[1] == 1 and event2[2] not in first_heard:
                    second_heard -= 1

            if event1[1] == 1:
                first_heard.remove(event1[2])

    return (max_heard, first_best, second_best)


# n = int(input())
# customers = []
# for _ in range(n):
#     time_in, time_out = map(int, input().split())
#     customers.append((time_in, time_out))

n = 4
customers = [(1, 11), (1, 3), (6, 15), (1, 6)]  # 3 1 6

# n = 1
# customers = [(1, 10)]  # 1 1 11

# n = 3
# customers = [(1, 10), (11, 20), (21, 30)]  # 2 1 11

res = find_two_times_for_advertisement(customers)
print(*res)
