def create_filled_dict(text):
    letters_count = {}

    for letter in text:
        if letter not in letters_count:
            letters_count[letter] = 0

    return letters_count


def find_longest_substring(text, k):
    max_len = 0
    first_letter = 0
    current_len = 0

    letters_count = create_filled_dict(text)

    right = 0
    for left in range(len(text)):
        while right < len(text) and letters_count[text[right]] < k:
            letters_count[text[right]] += 1
            current_len += 1
            right += 1

        if current_len > max_len:
            max_len = current_len
            first_letter = left

        letters_count[text[left]] -= 1

        current_len -= 1

    return (max_len, first_letter + 1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    text = input()

    # 2 1
    # k = 1
    # text = "abb"

    # 4 1
    # k = 2
    # text = "ababa"

    # 6 1
    # k = 1
    # text = "abcdef"

    # 9 2
    # k = 3
    # text = "aaaabvdveg"

    res = find_longest_substring(text, k)
    print(*res)
