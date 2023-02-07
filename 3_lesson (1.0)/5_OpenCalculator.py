# available_nums = list(map(int, input().split()))
# num = int(input())

# available_nums = [1, 2, 3]
# num = 1123

# available_nums = [1, 2, 3]
# num = 1001

available_nums = [5, 7, 3]
num = 123


def adjust_calculator(available_nums, num):
    needed = set(map(int, str(num)))
    available = set(available_nums)
    if needed == available:
        return 0
    else:
        return len(needed - available)


print(adjust_calculator(available_nums, num))
