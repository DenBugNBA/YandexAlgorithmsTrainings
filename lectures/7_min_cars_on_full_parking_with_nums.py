def is_parking_full(cars, n):
    events = []
    for i in range(len(cars)):
        time_in, time_out, place_from, place_to = cars[i]
        events.append(time_in, 1, place_to - place_from + 1, i)
        events.append(time_out, -1, place_to - place_from + 1, i)
    events.sort()

    occupied = 0

    min_cars = len(cars) + 1
    current_cars = 0

    for event in events:
        if event[1] == -1:
            occupied -= event[2]
            current_cars -= 1
        elif event[1] == 1:
            occupied += event[2]
            current_cars += 1

        if occupied == n and current_cars < min_cars:
            min_cars = current_cars

    current_nums = set()
    current_cars = 0

    for event in events:
        if event[1] == -1:
            occupied -= event[2]
            current_cars -= 1
            current_nums.remove(event[3])
        elif event[1] == 1:
            occupied += event[2]
            current_cars += 1
            current_nums.add(event[3])

        if occupied == n and current_cars == min_cars:
            return sorted(current_nums)

    return set()
