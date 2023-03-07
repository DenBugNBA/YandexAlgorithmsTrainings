def count_languages(pupils):
    all_pupils = set(pupils[0])
    all_languages = set(pupils[0])

    for i in range(1, len(pupils)):
        all_pupils &= set(pupils[i])
        for language in pupils[i]:
            all_languages.add(language)

    return all_pupils, all_languages


if __name__ == "__main__":
    n = int(input())

    pupils = []
    for _ in range(n):
        m = int(input())
        current = []
        for _ in range(m):
            current.append(input())
        pupils.append(current)

    # 1
    # English
    # 3
    # Russian
    # Japanese
    # English
    # pupils = [["Russian", "English", "Japanese"], ["Russian", "English"], ["English"]]

    res = count_languages(pupils)
    print(len(res[0]))
    for language in res[0]:
        print(language)
    print(len(res[1]))
    for language in res[1]:
        print(language)
