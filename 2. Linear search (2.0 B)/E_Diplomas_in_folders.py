if __name__ == "__main__":
    n = int(input())
    folders = list(map(int, input().split()))

    # 1
    # n = 2
    # folders = [2, 1]

    # 0
    # n = 0
    # folders = [1]

    max_time = 0
    sum_time = 0

    for diplomas_in_folder in folders:
        sum_time += diplomas_in_folder

        if diplomas_in_folder > max_time:
            max_time = diplomas_in_folder

    print(sum_time - max_time)
