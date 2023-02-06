def replace_extra_items(number):
    extra_items = ["-", "(", ")", "+"]
    for item in extra_items:
        number = number.replace(item, "")
    return number


def format_number(number):
    raw_number = replace_extra_items(number)
    if len(raw_number) == 7:  # only number
        return "495" + raw_number
    else:
        return raw_number[1:]


def is_same_number(number1, number2):
    number1 = format_number(number1)
    number2 = format_number(number2)
    if number1 == number2:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    new_number = input()
    number1 = input()
    number2 = input()
    number3 = input()

    # YES
    # YES
    # NO
    # new_number = "8(495)430-23-97"
    # number1 = "+7-4-9-5-43-023-97"
    # number2 = "4-3-0-2-3-9-7"
    # number3 = "8-495-430"

    # NO
    # YES
    # NO
    # new_number = "86406361642"
    # number1 = "83341994118"
    # number2 = "86406361642"
    # number3 = "83341994118"

    # YES
    # NO
    # YES
    # new_number = "+78047952807"
    # number1 = "+78047952807"
    # number2 = "+76147514928"
    # number3 = "88047952807"

    print(is_same_number(new_number, number1))
    print(is_same_number(new_number, number2))
    print(is_same_number(new_number, number3))
