def count_most_chemistry_team(professionalism):
    current_sum = 0
    max_sum = 0

    right = 0
    for left in range(len(professionalism)):
        while right < len(professionalism) and (
            left == right
            or professionalism[left] + professionalism[left + 1]
            >= professionalism[right]
        ):
            current_sum += professionalism[right]
            right += 1

        max_sum = max(max_sum, current_sum)
        current_sum -= professionalism[left]

    return max_sum


professionalism = [1, 1, 3, 3, 4, 6, 11]
print(count_most_chemistry_team(professionalism))
