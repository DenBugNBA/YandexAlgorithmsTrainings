n = int(input())
possible_nums = set(range(1, n + 1))

while True:
    request_arr = input()

    if request_arr == "HELP":
        print(*sorted(possible_nums))
        break

    else:
        request_arr = set(map(int, request_arr.split()))

        answer = input()

        if answer == "YES":
            possible_nums = possible_nums & request_arr
        else:
            possible_nums -= request_arr
