def get_power_costs(conditioners):
    power_costs = {}

    for power, price in conditioners:
        if power not in power_costs:
            power_costs[power] = price
        else:
            if price < power_costs[power]:
                power_costs[power] = price

    return power_costs


def optimize_power_costs(power_costs):
    sorted_powers = sorted(power_costs.keys(), reverse=True)
    min_cost = power_costs[sorted_powers[0]]

    for i in range(1, len(sorted_powers)):
        current_power = sorted_powers[i]
        current_cost = power_costs[current_power]
        if current_cost < min_cost:
            min_cost = current_cost
        else:
            del power_costs[current_power]

    return power_costs


def count_minimun_cost(required_powers, optimized_power_costs):
    cost = 0
    availaible_powers = sorted(optimized_power_costs.keys())
    required_powers_sorted = sorted(required_powers)

    current_power_index = 0
    for current_required in required_powers_sorted:
        while (
            current_power_index < len(availaible_powers)
            and current_required > availaible_powers[current_power_index]
        ):
            current_power_index += 1

        power = availaible_powers[current_power_index]
        cost += optimized_power_costs[power]

    return cost


if __name__ == "__main__":
    n = int(input())
    required_powers = list(map(int, input().split()))
    m = int(input())
    conditioners = []
    for _ in range(m):
        power, price = map(int, input().split())
        conditioners.append((power, price))

    # 1000
    # required_powers = [800]
    # conditioners = [(800, 1000)]

    # 13
    # required_powers = [1, 2, 3]
    # conditioners = [(1, 10), (1, 5), (10, 7), (2, 3)]

    power_costs = get_power_costs(conditioners)
    optimized_power_costs = optimize_power_costs(power_costs)
    print(count_minimun_cost(required_powers, optimized_power_costs))
