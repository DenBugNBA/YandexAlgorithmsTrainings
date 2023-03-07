if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    candidates = {}
    for line in lines:
        surname, number_of_votes = line.split()
        if surname not in candidates:
            candidates[surname] = 0
        candidates[surname] += int(number_of_votes)

    for surname in sorted(candidates.keys()):
        print(f"{surname} {candidates[surname]}")
