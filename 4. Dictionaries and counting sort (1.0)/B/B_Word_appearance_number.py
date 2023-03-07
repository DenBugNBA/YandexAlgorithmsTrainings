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


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    # 0 0 1 0 0
    # lines = ["one two one tho three"]

    # 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0
    # lines = [
    #     "She sells sea shells on the sea shore;",
    #     "The shells that she sells are sea shells I'm sure.",
    #     "So if she sells sea shells on the sea shore,",
    #     "I'm sure that the shells are sea shore shells.",
    # ]

    # 0 0 1 0
    # lines = ['aba aba; aba @?"']

    res = count_word_appearance(lines)
    print(*res)
