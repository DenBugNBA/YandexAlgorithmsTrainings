# ищет первое хорошее
# mid - левое из двух
def left_binary_search(left, right, check, params):
    while left < right:
        mid = (left + right) // 2
        if check(mid, params):
            right = mid
        else:
            left = mid + 1

    return left


# ищет последнее хорошее
# mid - правое из двух
def left_binary_search(left, right, check, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, params):
            left = mid
        else:
            right = mid - 1

    return left
