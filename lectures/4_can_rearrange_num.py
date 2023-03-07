def count_digits(num):
    digits_count = [0] * 10

    while num > 0:
        last_digit = num % 10
        digits_count[last_digit] += 1
        num //= 10

    return digits_count


def can_rearrange_num(num1, num2):
    digits1 = count_digits(num1)
    digits2 = count_digits(num2)

    for digit in range(10):
        if digits1[digit] != digits2[digit]:
            return False
    return True


num1 = 2021
num2 = 1202

print(can_rearrange_num(num1, num2))
