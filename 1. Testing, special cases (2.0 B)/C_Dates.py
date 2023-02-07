if __name__ == "__main__":
    x, y, z = map(int, input().split())

    # 0
    # x, y, z = 1, 2, 2003

    # 1
    # x, y, z = 2, 29, 2008

    if x > 12 or y > 12 or (x == y):
        print(1)
    else:
        print(0)
