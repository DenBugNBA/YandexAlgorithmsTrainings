def count_optimal_time(m, helpers_params):
    events = []
    current_params = []

    for i in range(len(helpers_params)):
        # 0: кол-во минут на шарик, 1: сколько шаров подряд до перерыва, 2: время перерыва
        t, _, _ = helpers_params[i]

        # 0: время события, 1: id события, 2: индекс помощника
        events.append((t, -1, i))

        # 0: всего надутых помощником, 1: текущий счётчик надутых, 2: время последнего надутия шарика
        current_params.append([0, 0, 0, 0])
    events.sort()

    current_baloons = 0
    i = 0
    while current_baloons < m:
        # надут шарик
        if events[i][1] == -1:
            current_baloons += 1

            helper_index = events[i][2]
            current_params[helper_index][0] += 1
            current_params[helper_index][1] += 1
            current_params[helper_index][2] = events[i][0]

            if current_params[helper_index][1] == helpers_params[helper_index][1]:
                current_params[helper_index][1] = 0
                events.append(
                    (events[i][0] + helpers_params[helper_index][2], 1, helper_index)
                )
            else:
                events.append(
                    (events[i][0] + helpers_params[helper_index][0], -1, helper_index)
                )

        # прошел перерыв
        elif events[i][1] == 1:
            helper_index = events[i][2]

            events.append(
                (events[i][0] + helpers_params[helper_index][0], -1, helper_index)
            )

        events.sort()
        i += 1

    last_hepler_index = events[i - 1][2]
    result_time = current_params[last_hepler_index][2]

    result_helper_counter = []
    for i in range(len(current_params)):
        result_helper_counter.append(current_params[i][0])

    return result_time, result_helper_counter


# m, n = map(int, input().split())
# helpers_params = []
# for _ in range(n):
#     t, z, y = map(int, input().split())
#     helpers_params.append((t, z, y))

# 1
# 0 1
m, n = 1, 2
helpers_params = [(2, 1, 1), (1, 1, 2)]

# 1
# 1 1
# m, n = 2, 2
# helpers_params = [(1, 1, 1), (1, 1, 1)]

# 6
# 2 1
# m, n = 3, 2
# helpers_params = ((2, 1, 2), (1, 1, 10))

# 0
# 0 0
# m, n = 0, 2
# helpers_params = ((2, 1, 2), (1, 1, 10))

# 6
# 5 2
# m, n = 7, 2
# helpers_params = ((1, 3, 1), (2, 3, 1))

# 5
# 4 2
# m, n = 6, 2
# helpers_params = ((1, 3, 1), (2, 3, 1))

# 4
# 3 2
# m, n = 5, 2
# helpers_params = ((1, 3, 1), (2, 3, 1))

# 6
# 3 0
# m, n = 3, 2
# helpers_params = ((2, 3, 1), (10, 1, 1))

# 8
# 4 2 4
# m, n = 10, 3
# helpers_params = [(1, 2, 3), (3, 10, 3), (2, 4, 3)]

# 4
# 2 1
# m, n = 3, 2
# helpers_params = [(2, 2, 5), (1, 1, 10)]

result_time, result_helper_counter = count_optimal_time(m, helpers_params)
print(result_time)
print(*result_helper_counter)
