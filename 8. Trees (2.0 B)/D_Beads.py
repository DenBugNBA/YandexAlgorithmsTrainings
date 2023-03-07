from collections import deque


def create_connection(first, second, beads):
    if first not in beads:
        beads[first] = []
    beads[first].append(second)


def count_connected_beads(bead, beads):
    current_connected = 0

    beads_queue = deque([bead])
    seen_beads = set()

    while beads_queue:
        n = len(beads_queue)

        for _ in range(n):
            current_bead = beads_queue.popleft()
            seen_beads.add(current_bead)

            for new_bead in beads[current_bead]:
                if new_bead not in seen_beads:
                    beads_queue.append(new_bead)

        current_connected += 1
    return current_connected


if __name__ == "__main__":
    n = int(input())

    beads = {}

    for _ in range(n - 1):
        first, second = map(int, input().split())
        create_connection(first, second, beads)
        create_connection(second, first, beads)

    max_connected = 0

    for bead in beads:
        if len(beads[bead]) == 1:
            current_connected = count_connected_beads(bead, beads)
            max_connected = max(max_connected, current_connected)

    print(max_connected)
