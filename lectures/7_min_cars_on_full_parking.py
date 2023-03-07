def is_parking_full(cars, n):
    events = []
    for car in cars:
        time_in, time_out, place_from, place_to = car
        events.append((time_in, 1, place_to - place_from + 1))
        events.append((time_out, -1, place_to - place_from + 1))

    events.sort()

    occupied = 0

    min_cars = len(cars) + 1
    current_cars = 0

    for event in events:
        if event[1] == -1:
            occupied -= event[2]
            current_cars -= 1
        elif events[1] == 1:
            occupied += event[2]
            current_cars += 1

        if occupied == n:
            min_cars = min(min_cars, current_cars)

    return min_cars
