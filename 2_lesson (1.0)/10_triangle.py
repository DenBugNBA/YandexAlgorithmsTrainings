# n = int(input())
# prev = float(input())
# attempts = []
# for i in range(n - 1):
#     line = input().split()
#     attempts.append((float(line[0]), line[1]))

# prev = 440
# attempts = [(220, "closer"), (300, "further")]

# prev = 554
# attempts = [(880, "further"), (440, "closer"), (622, "closer")]

prev = 800
attempts = [
    (600, "further"),
    (1900, "further"),
    (1900, "further"),
    (1900, "further"),
    (2000, "further"),
    (1000, "closer"),
]

# prev = 300
# attempts = [(900, "further")]


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


res = determine_possible_range(prev, attempts)
print(res[0], res[1])
