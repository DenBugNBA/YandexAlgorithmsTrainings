def check_is_valid_length(length, params):
    k, sections = params
    equal_sections_count = 0
    for section_length in sections:
        equal_sections_count += section_length // length

    return equal_sections_count >= k


def binary_search(left, right, check, params):
    while left < right:
        mid = (left + right + 1) // 2

        if check(mid, params):
            left = mid
        else:
            right = mid - 1

    return left


# n, k = map(int, input().split())
# sections = []
# for _ in range(n):
#     sections.append(int(input()))

n, k = 4, 11
sections = [802, 743, 457, 539]

print(binary_search(0, 10**30, check_is_valid_length, (k, sections)))
