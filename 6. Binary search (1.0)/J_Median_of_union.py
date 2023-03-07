def count_left_median(arr1, arr2):
    current_num = 0
    first = second = 0

    for _ in range(len(arr1)):
        if first != len(arr1) and (second == len(arr2) or arr1[first] <= arr2[second]):
            current_num = arr1[first]
            first += 1
        else:
            current_num = arr2[second]
            second += 1

    return current_num


def find_left_median_of_union(arrs):
    for i in range(len(arrs)):
        right = i + 1
        for j in range(right, len(arrs)):
            print(count_left_median(arrs[i], arrs[j]))


if __name__ == "__main__":
    n, l = map(int, input().split())
    arrs = []
    for _ in range(n):
        arrs.append(list(map(int, input().split())))

    # 7
    # 10
    # 9
    # n, l = 3, 6
    # arrs = [[1, 4, 7, 10, 13, 16], [0, 2, 5, 9, 14, 20], [1, 7, 16, 16, 21, 22]]

    find_left_median_of_union(arrs)
