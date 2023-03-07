def keyboard_info(clicks_hold, clicks_made):
    for key in clicks_made:
        clicks_hold[key - 1] -= 1

    for left_clicks in clicks_hold:
        if left_clicks >= 0:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    n = input()
    clicks_hold = list(map(int, input().split()))
    k = input()
    clicks_made = list(map(int, input().split()))

    # YES
    # NO
    # NO
    # NO
    # YES
    # clicks_hold = [1, 50, 3, 4, 3]
    # clicks_made = [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5, 5, 4, 5]

    keyboard_info(clicks_hold, clicks_made)
