if __name__ == "__main__":
    arr = list(map(int, input().split()))

    seen = set()
    repetitions = set()

    for num in arr:
        if num in seen:
            repetitions.add(num)
        else:
            seen.add(num)

    unique_nums = []

    for num in arr:
        if num not in repetitions:
            unique_nums.append(num)

    print(*unique_nums)
