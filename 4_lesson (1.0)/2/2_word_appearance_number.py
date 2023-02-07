lines = []
with open("input.txt") as f:
    lines = f.readlines()

# lines = [
#     "She sells sea shells on the sea shore;",
#     "The shells that she sells are sea shells I'm sure.",
#     "So if she sells sea shells on the sea shore,",
#     "I'm sure that the shells are sea shore shells.",
# ]

# lines = ["one two one tho three"]

# lines = ['aba aba; aba @?"']


def count_word_appearance(lines):
    result = []
    words_count = {}

    for line in lines:
        words = line.split()

        for word in words:
            if word not in words_count:
                words_count[word] = 0

            result.append(words_count[word])
            words_count[word] += 1

    return result


res = count_word_appearance(lines)
print(*res)
