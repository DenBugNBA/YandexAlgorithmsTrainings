if __name__ == "__main__":
    n = int(input())
    student_houses = list(map(int, input().split()))

    # 3
    # n = 4
    # student_houses = [1, 2, 3, 4]

    # 0
    # n = 3
    # student_houses = [-1, 0, 1]

    index = n // 2
    print(student_houses[index])
