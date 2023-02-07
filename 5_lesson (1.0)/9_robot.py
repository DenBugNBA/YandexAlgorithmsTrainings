def count_valid_ways(operations, k):
    valid_ways_count = 0

    current_series = 0
    for i in range(k, len(operations)):
        if operations[i] == operations[i - k]:
            current_series += 1
            valid_ways_count += current_series
        else:
            current_series = 0

    return valid_ways_count


# k = int(input())
# operations = input()

k = 2
operations = "zabacabab"  # 5

# k = 3
# operations = "abcabcac"  # 10

# k = 2
# operations = "abc"  # 0

print(count_valid_ways(operations, k))
