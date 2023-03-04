def read_and_enum():
    return sorted(enumerate(list(map(int, input().split()))[1:]), key=lambda x: x[1])


if __name__ == "__main__":
    s = int(input())
    a = read_and_enum()
    b = read_and_enum()
    c = read_and_enum()

    c.sort(key=lambda x: (x[1], -x[0]))

    flag = False

    for a_pos, a_val in a:
        c_pos = len(c) - 1
        for b_pos, b_val in b:
            while c_pos > 0 and a_val + b_val + c[c_pos][1] > s:
                c_pos -= 1
            if a_val + b_val + c[c_pos][1] == s and (
                not flag or (a_pos, b_pos, c_pos) < ans
            ):
                ans = a_pos, b_pos, c[c_pos][0]
                flag = True

    if flag:
        print(*ans)
    else:
        print(-1)
