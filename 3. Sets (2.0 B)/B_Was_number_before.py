if __name__ == "__main__":
    arr = list(map(int, input().split()))

    seen = set()

    for num in arr:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)
