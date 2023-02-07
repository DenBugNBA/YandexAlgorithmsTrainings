from string import ascii_uppercase, ascii_lowercase


def find_emphasis_index(word):
    for i in range(len(word)):
        if word[i] not in ascii_lowercase:
            return i


def is_valid_amount_emphasis(word):
    emphasis_count = 0

    for letter in word:
        if letter in ascii_uppercase:
            emphasis_count += 1

    return emphasis_count == 1


def count_mistakes(text):
    mistakes_count = 0

    for word in text.split():
        if is_valid_amount_emphasis(word):
            word_lower = word.lower()
            if word_lower in dictionary:
                if find_emphasis_index(word) not in dictionary[word_lower]:
                    mistakes_count += 1
        else:
            mistakes_count += 1

    return mistakes_count


# n = int(input())
# dictionary = {}
# for _ in range(n):
#     word = input()
#     word_lower = word.lower()
#     if word_lower not in dictionary:
#         dictionary[word_lower] = []
#     index = find_emphasis_index(word)
#     dictionary[word_lower].append(index)
# text = input()

dictionary = {"cannot": [1, 4], "found": [1], "page": [1]}
# text = "thE pAge cAnnot be found"  # 2
text = "The PAGE cannot be found"  # 4

# dictionary = {}
# text = "Aa a"

print(count_mistakes(text))
