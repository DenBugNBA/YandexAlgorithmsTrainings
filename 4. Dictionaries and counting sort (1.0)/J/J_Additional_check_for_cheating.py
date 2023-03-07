from string import ascii_letters, digits


def parse_lines(lines, c, available_characters):
    words = []

    for line in lines:
        if c == "no":
            line = line.lower()

        current_sequence = []

        for symbol in line.strip():
            if symbol in available_characters:
                current_sequence.append(symbol)
            else:
                if current_sequence:
                    words.append("".join(current_sequence))
                current_sequence = []

        if current_sequence:
            words.append("".join(current_sequence))

    return words


def is_identifier(word, d, keywords):
    if word in keywords or (d == "no" and word[0] in digits):
        return False

    for letter in word:
        if letter not in digits:
            return True

    return False


def count_identifiers(words, d, keywords):
    identifiers_count = {}

    for word in words:
        if is_identifier(word, d, keywords):
            if word not in identifiers_count:
                identifiers_count[word] = 0
            identifiers_count[word] += 1

    return identifiers_count


def find_most_frequent_identifier(identifiers, words):
    count_most_frequent = 0

    for count in identifiers.values():
        if count > count_most_frequent:
            count_most_frequent = count

    most_frequent_identifiers = []

    for identifier, count in identifiers.items():
        if count == count_most_frequent:
            most_frequent_identifiers.append(identifier)

    if len(most_frequent_identifiers) == 1:
        return most_frequent_identifiers[0]
    else:
        for word in words:
            if word in most_frequent_identifiers:
                return word


if __name__ == "__main__":
    with open("input.txt") as f:
        # n - число ключевых слов
        # c - чувствительны к регистру
        # d - идентификаторы могут начинаться с цифры
        n, c, d = f.readline().split()
        keywords = []

        for _ in range(int(n)):
            keyword = f.readline().strip()

            if c == "no":
                keywords.append(keyword.lower())
            else:
                keywords.append(keyword)

        lines = f.readlines()

    available_characters = ascii_letters + digits + "_"

    words = parse_lines(lines, c, available_characters)
    identifiers = count_identifiers(words, d, keywords)
    print(find_most_frequent_identifier(identifiers, words))
