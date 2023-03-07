def calculate_degree_of_proximity(genome1, genome2):
    bases2 = set()
    for i in range(len(genome2) - 1):
        bases2.add(genome2[i : i + 2])

    degree_of_proximity = 0

    for i in range(len(genome1) - 1):
        if genome1[i : i + 2] in bases2:
            degree_of_proximity += 1

    return degree_of_proximity


if __name__ == "__main__":
    genome1 = input()
    genome2 = input()

    # 4
    # genome1 = "ABBACAB"
    # genome2 = "BCABB"

    print(calculate_degree_of_proximity(genome1, genome2))
