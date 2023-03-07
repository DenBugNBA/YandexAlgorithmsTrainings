if __name__ == "__main__":
    n = int(input())
    synonyms = {}
    for _ in range(n):
        a, b = input().split()
        synonyms[a] = b
        synonyms[b] = a
    print(synonyms[input()])
