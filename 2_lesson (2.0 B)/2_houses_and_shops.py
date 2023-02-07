nums = list(map(int, input().split()))

houses = []

current_distance = 10

for num in nums:
    current_distance += 1

    if num == 2:
        current_distance = 0

    elif num == 1:
        houses.append(current_distance)

current_distance = 10
house_index = 1

for num in nums[::-1]:
    current_distance += 1

    if num == 2:
        current_distance = 0

    elif num == 1:
        if current_distance < houses[-house_index]:
            houses[-house_index] = current_distance
        house_index += 1

max_distance = 0

for distance in houses:
    if distance > max_distance:
        max_distance = distance

print(max_distance)
