from collections import Counter, defaultdict

"""
w - некоторое слово
s - последовательность
"""


def count_possible_entries(w, s):
    pattern = Counter(w)
    pattern_len = len(w)
    window = defaultdict(int)

    count = 0

    start = 0
    for end in range(len(s)):
        letter = s[end]
        window[letter] += 1

        if end - start + 1 == pattern_len:
            if window == pattern:
                count += 1

            start_letter = s[start]
            window[start_letter] -= 1

            if window[start_letter] == 0:
                del window[start_letter]

            start += 1

    return count


if __name__ == "__main__":
    w_len, s_len = map(int, input().split())
    w = input()
    s = input()

    # 2
    # w = "cAda"
    # s = "AbrAcadAbRa"

    print(count_possible_entries(w, s))
