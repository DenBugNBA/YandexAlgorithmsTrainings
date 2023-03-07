def calculate_method_of_distributing_tickets(coordinates, d):
    events = []

    for i in range(len(coordinates)):
        events.append((coordinates[i], 0, i))
    events.sort()

    result_types = [0] * len(coordinates)
    queue = []
    current_type = 0
    one_pair = 0

    for i in range(len(events)):
        if i != 0 and events[i - 1][0] + d < events[i][0]:
            if (1, one_pair) in queue:
                queue.remove((1, one_pair))

            one_pair = events[i][0]
            queue.append((1, events[i][0]))
            result_types[events[i][2]] = 1

        elif queue != [] and events[i][0] - d > queue[0][1]:
            pop_type, _ = queue.pop(0)
            queue.append((pop_type, events[i][0]))
            result_types[events[i][2]] = pop_type

            if pop_type == 1:
                one_pair = events[i][0]

        else:
            current_type += 1
            queue.append((current_type, events[i][0]))
            result_types[events[i][2]] = current_type

            if current_type == 1:
                one_pair = events[i][0]

    return result_types


def print_result(coordinates, d):
    result_types = calculate_method_of_distributing_tickets(coordinates, d)
    types_amount = max(result_types)
    print(types_amount)
    print(*result_types)


if __name__ == "__main__":
    n, d = map(int, input().split())
    coordinates = list(map(int, input().split()))

    # 2
    # 1 1 2 2
    # n, d = 4, 1
    # coordinates = [11, 1, 12, 2]

    # 1
    # 1 1 1 1
    # n, d = 4, 0
    # coordinates = [11, 1, 12, 2]

    # 5
    # 1 2 3 1 4 2 5 3
    # n, d = 8, 5
    # coordinates = [1, 3, 5, 7, 8, 9, 10, 11]

    # 2
    # 1 2 1 2 1 1
    # n, d = 3, 2
    # coordinates = [1, 3, 5, 7, 9, 12]

    # 4
    # 1 2 3 1 4
    # n, d = 5, 5
    # coordinates = [1, 3, 5, 7, 8]

    # 2
    # 1 2 1 2
    # n, d = 4, 1
    # coordinates = [1, 2, 11, 12]

    # 1
    # 1 1 1 1 1 1
    # n, d = 6, 1
    # coordinates = [1, 3, 5, 7, 9, 11]

    # 2
    # 1 2 1 2
    # n, d = 3, 2
    # coordinates = [1, 3, 5, 7]

    # 1
    # 1
    # n, d = 1, 0
    # coordinates = [10]

    print_result(coordinates, d)
