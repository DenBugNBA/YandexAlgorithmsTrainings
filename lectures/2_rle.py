"""
Кодирование длин серий (англ. run-length encoding, RLE) или кодирование
повторов — алгоритм сжатия данных, заменяющий повторяющиеся символы (серии) на
один символ и число его повторов.
"""


def rle(s):
    current_letter = None
    current_length = 0
    result = []

    for letter in s:
        if current_letter == letter:
            current_length += 1
        else:
            count = current_length if current_length > 1 else ""
            result.append(f"{current_letter}{count}")
            current_letter = letter
            current_length = 1

    count = current_length if current_length > 1 else ""
    result.append(f"{current_letter}{count}")

    return "".join(result[1:])


print(rle("DAAAABBBCCCADDDDDDDDDDDBBBBBBBBB"))
print(rle(""))
print(rle("ABCDEF"))
