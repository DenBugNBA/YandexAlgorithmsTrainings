if __name__ == "__main__":
    n = int(input())

    colors_sum = {}
    for _ in range(n):
        color_num, number = map(int, input().split())

        if color_num not in colors_sum:
            colors_sum[color_num] = 0
        colors_sum[color_num] += number

    for color_num in sorted(colors_sum.keys()):
        print(f"{color_num} {colors_sum[color_num]}")
