# lines = []
# with open("input.txt") as f:
#     lines = f.readlines()

lines = ["q w e r t y u i o p", "a s d f g h j k l" "z x c v b n m"]

# text = "apple orange banana banana orange"

# text = "oh you touch my tralala mmm my ding ding dong"


def find_most_frequent_word(lines):
    words_count = {}

    for line in lines:
        for word in line.split():
            if word not in words_count:
                words_count[word] = 0
            words_count[word] += 1

    max_count = 0
    max_word = ""
    for word in words_count.keys():
        if words_count[word] > max_count:
            max_word = word
            max_count = words_count[word]
        elif words_count[word] == max_count:
            max_word = min(max_word, word)
            max_count = words_count[max_word]

    return max_word


print(find_most_frequent_word(lines))
