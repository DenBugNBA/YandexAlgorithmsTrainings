def count_students_without_observation(n, observations):
    events = []

    for i in range(len(observations)):
        observe_from, observe_to = observations[i]
        events.append((observe_from, -1))
        events.append((observe_to, 1))
    events.sort()

    observed_students = 0
    current_start = 0
    amount_starts = 0

    for event in events:
        if event[1] == -1:
            if amount_starts == 0:
                current_start = event[0]
            amount_starts += 1
        elif event[1] == 1:
            if amount_starts == 1:
                observed_students += event[0] - current_start + 1
                amount_starts = 0
            else:
                amount_starts -= 1

    return n - observed_students


if __name__ == "__main__":
    n, m = map(int, input().split())
    observations = []
    for i in range(m):
        observe_from, observe_to = map(int, input().split())
        observations.append((observe_from, observe_to))

    # 5
    # n, m = 10, 3
    # observations = [(1, 3), (2, 4), (9, 9)]

    # 8
    # n, m = 10, 2
    # observations = [(1, 1), (1, 2)]

    print(count_students_without_observation(n, observations))
