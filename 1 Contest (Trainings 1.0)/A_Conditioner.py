def count_temperature(troom, tcond, mode):
    if mode == "fan":
        return troom
    elif mode == "auto":
        return tcond
    elif mode == "heat":
        return max(troom, tcond)
    else:
        return min(troom, tcond)


if __name__ == "__main__":
    troom, tcond = list(map(int, input().split()))
    mode = input()

    # 20
    # troom, tcond = 10, 20
    # mode = "heat"

    # 10
    # troom, tcond = 10, 20
    # mode = "freeze"

    print(count_temperature(troom, tcond, mode))
