def find_min_amount_of_buses(n, m, timetable):
    events = []
    buses_balance = [0] * (n + 1)
    overnights = 0

    for i in range(m):
        hours_from = timetable[i][1][0]
        minutes_from = timetable[i][1][1]
        city_from = timetable[i][0]
        city_to = timetable[i][2]
        hours_to = timetable[i][3][0]
        minutes_to = timetable[i][3][1]

        if hours_from > hours_to or (
            hours_from == hours_to and minutes_from > minutes_to
        ):
            overnights += 1

        buses_balance[city_from] -= 1
        buses_balance[city_to] += 1

        events.append((hours_from, minutes_from, 1, city_from, city_to))
        events.append((hours_to, minutes_to, -1, city_to))

    balanced_flag = True
    for i in range(n):
        if buses_balance[i] != 0:
            balanced_flag = False

    if not balanced_flag:
        return -1
    else:
        events.sort()

        cities_current_buses = [0] * (n + 1)

        for i in range(2 * m):
            # прибытие автобуса
            if events[i][2] == -1:
                city_to = events[i][3]
                cities_current_buses[city_to] += 1

            # отправление автобуса
            if events[i][2] == 1:
                *_, city_from, city_to = events[i]
                if cities_current_buses[city_from] != 0:
                    cities_current_buses[city_from] -= 1

        buses_needed = 0

        for i in range(n + 1):
            buses_needed += cities_current_buses[i]
        buses_needed += overnights

        return buses_needed


# n, m = map(int, input().split())
# timetable = []
# for i in range(m):
#     data = input().split()

#     city_from = int(data[0])
#     time_from = (int(data[1][:2]), int(data[1][3:]))

#     city_to = int(data[2])
#     time_to = (int(data[3][:2]), int(data[3][3:]))

#     timetable.append((city_from, time_from, city_to, time_to))

# print(timetable)

n, m = 2, 2
timetable = [(2, (20, 0), 1, (10, 0)), (1, (8, 0), 2, (21, 0))]  # 3

# n, m = 2, 2
# timetable = [(1, (9, 0), 2, (20, 0)), (2, (20, 0), 1, (9, 0))]  # 1

# n, m = 3, 4
# timetable = [
#     (3, (3, 52), 1, (8, 50)),
#     (1, (18, 28), 3, (21, 53)),
#     (2, (3, 58), 3, (9, 0)),
#     (3, (14, 59), 2, (21, 13)),
# ]  # 2

# n, m = 2, 2
# timetable = [(1, (9, 0), 2, (20, 0)), (1, (20, 0), 2, (9, 0))]  # -1

# n, m = 2, 1
# timetable = [(1, (9, 0), 2, (20, 0))]  # -1

# n, m = 2, 2
# timetable = [(1, (10, 0), 2, (9, 59)), (2, (10, 2), 1, (10, 1))]  # 3

# n, m = 2, 1
# timetable = [(1, (9, 0), 2, (15, 30))]  # -1

# n, m = 5, 5
# timetable = [
#     (1, (9, 0), 2, (14, 30)),
#     (3, (23, 45), 1, (6, 50)),
#     (2, (14, 30), 3, (20, 50)),
#     (4, (9, 0), 5, (21, 0)),
#     (5, (10, 0), 4, (20, 0)),
# ]  # 3

print(find_min_amount_of_buses(n, m, timetable))
