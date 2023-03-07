def group_words(arr):
    letters = {}

    for word in arr:
        sorted_word = "".join(sorted(word))

        if sorted_word not in letters:
            letters[sorted_word] = []
        letters[sorted_word].append(word)

    return [letters[key] for key in letters]


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_words(arr))


def key_by_word(word):
    letters = {}

    for letter in word:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    letters_list = []

    for letter in sorted(letters.keys()):
        letters_list.append(letter)
        letters_list.append(str(letters[letter]))

    return "".join(letters_list)


def group_words_optimized(arr):
    groups = {}

    for word in arr:
        group_key = key_by_word(word)
        print(group_key)

        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(word)

    return [groups[key] for key in groups]


arr1 = [
    "...............................................................................................................",
    ".1",
]  # breaks

print(group_words_optimized(arr1))
