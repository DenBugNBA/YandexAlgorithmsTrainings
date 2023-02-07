with open("input.txt") as f:
    lines = f.readlines()

words_count = {}

for line in lines:
    for word in line.split():
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += 1

words_count_tuples = []

for word in words_count.keys():
    words_count_tuples.append((words_count[word], word))
words_count_tuples.sort(key=lambda x: (-x[0], x[1]))

for _, word in words_count_tuples:
    print(word)
