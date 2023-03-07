def adjust_calculator(available_nums, num):
    needed = set(map(int, str(num)))
    available = set(available_nums)
    if needed == available:
        return 0
    else:
        return len(needed - available)


if __name__ == "__main__":
    available_nums = list(map(int, input().split()))
    num = int(input())

    # 0
    # available_nums = [1, 2, 3]
    # num = 1123

    # 1
    # available_nums = [1, 2, 3]
    # num = 1001

    # 2
    # available_nums = [5, 7, 3]
    # num = 123

    print(adjust_calculator(available_nums, num))
