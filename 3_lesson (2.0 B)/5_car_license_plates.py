m = int(input())
statements = []
for _ in range(m):
    statements.append(input())
n = int(input())
license_plates = []
for _ in range(n):
    license_plates.append(input())

matches_count = [0] * n

for i in range(n):
    for statement in statements:
        if len(set(statement) & set(license_plates[i])) == len(set(statement)):
            matches_count[i] += 1

max_matches = 0

for current_count in matches_count:
    if current_count > max_matches:
        max_matches = current_count

for i in range(n):
    if matches_count[i] == max_matches:
        print(license_plates[i])
