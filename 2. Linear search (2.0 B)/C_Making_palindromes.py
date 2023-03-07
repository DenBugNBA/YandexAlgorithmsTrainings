if __name__ == "__main__":
    line = input()

    cost = 0

    for i in range(len(line) // 2):
        if line[i] != line[-(i + 1)]:
            cost += 1

    print(cost)
