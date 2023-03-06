def determine_possible_range(prev, attempts):
    min_frequency = 30.0
    max_frequency = 4000.0

    for freq, res in attempts:
        if freq == prev:
            continue

        if res == "closer":
            if freq > prev:
                min_frequency = max(min_frequency, (prev + freq) / 2)
            else:
                max_frequency = min(max_frequency, (prev + freq) / 2)
        else:
            if freq > prev:
                max_frequency = min(max_frequency, (prev + freq) / 2)
            else:
                min_frequency = max(min_frequency, (prev + freq) / 2)

        prev = freq

    return min_frequency, max_frequency


if __name__ == "__main__":
    n = int(input())
    prev = float(input())
    attempts = []
    for i in range(n - 1):
        line = input().split()
        attempts.append((float(line[0]), line[1]))

    # 30.0 260.0
    # prev = 440
    # attempts = [(220, "closer"), (300, "further")]

    # 531.0 660.0
    # prev = 554
    # attempts = [(880, "further"), (440, "closer"), (622, "closer")]

    # 700.0 1250.0
    # prev = 800
    # attempts = [
    #     (600, "further"),
    #     (1900, "further"),
    #     (1900, "further"),
    #     (1900, "further"),
    #     (2000, "further"),
    #     (1000, "closer"),
    # ]

    # 30.0 600.0
    # prev = 300
    # attempts = [(900, "further")]

    res = determine_possible_range(prev, attempts)
    print(*res)
