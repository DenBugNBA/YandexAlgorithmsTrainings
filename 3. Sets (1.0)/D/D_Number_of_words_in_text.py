def count_words(lines):
    words = []
    for line in lines:
        words_line = line.split()
        words.extend(words_line)
    return len(set(words))


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    # 19
    # lines = [
    #     "She sells sea shells on the sea shore;",
    #     "The shells that she sells are sea shells I'm sure.",
    #     "So if she sells sea shells on the sea shore,",
    #     "I'm sure that the shells are sea shore shells.",
    # ]

    print(count_words(lines))
