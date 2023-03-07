s = "ababa"
s1 = "abbbaaa"


def most_frequent_symb(s):  # O(n)
    symbols_freq = dict()
    for letter in s:
        if letter not in symbols_freq:
            symbols_freq[letter] = 0
        symbols_freq[letter] += 1

    max_freq = 0
    max_symb = ""
    for letter in symbols_freq:
        if symbols_freq[letter] > max_freq:
            max_freq = symbols_freq[letter]
            max_symb = letter

    return max_symb


print(most_frequent_symb(s))
print(most_frequent_symb(s1))
