def is_correct_bracket_sequence(s):
    current_opening_brackets = 0

    for bracket in s:
        if bracket == "(":
            current_opening_brackets += 1
        else:
            if current_opening_brackets == 0:
                return "NO"
            else:
                current_opening_brackets -= 1

    return "YES" if current_opening_brackets == 0 else "NO"


if __name__ == "__main__":
    s = input()
    print(is_correct_bracket_sequence(s))
