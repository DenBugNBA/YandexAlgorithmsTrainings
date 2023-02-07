def count_min_stations(n, station_in, station_out):
    station_diff = abs(station_in - station_out) - 1

    return min(station_diff, n - (station_diff + 2))


if __name__ == "__main__":
    n, station_in, station_out = map(int, input().split())

    # 0
    # n, station_in, station_out = 100, 5, 6

    # 1
    # n, station_in, station_out = 10, 1, 9

    # 0
    # n, station_in, station_out = 10, 1, 10

    # 1
    # n, station_in, station_out = 10, 2, 10

    # 0
    # n, station_in, station_out = 3, 3, 1

    # 4
    # n, station_in, station_out = 10, 5, 10

    # 3
    # n, station_in, station_out = 10, 3, 9

    # 3
    # n, station_in, station_out = 10, 9, 3

    # 0
    # n, station_in, station_out = 2, 1, 2

    # 0
    # n, station_in, station_out = 2, 2, 1

    print(count_min_stations(n, station_in, station_out))
